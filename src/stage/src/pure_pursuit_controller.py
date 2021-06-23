#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
from math import pow, atan2, sqrt, atan, cos, sin
import tf.transformations
from stage.srv import xygoal
from visualization_msgs.msg import Marker


pi=3.141592653589793
distancia_lookahead=float(rospy.get_param('/pure_pursuit_controller/lookahead', 1.0)) #distancia lookahead en metros
debug=int(rospy.get_param('/pure_pursuit_controller/debug_level', 5)) #nivel de debug
velocidad= float(rospy.get_param('/pure_pursuit_controller/velocidad', 0.5))
def debug_level(number):
    if number==0:
        return rospy.NONE
    if number==1:
        return rospy.FATAL
    if number==2:
        return rospy.ERROR
    if number==3:
        return rospy.INFO
    if number==4:
        return rospy.WARN
    if number==5:
        return rospy.DEBUG

class node:
    def __init__(self, x, y, last):
        self.x=x
        self.y=y
        if last!=None:
            self.theta=atan2(y-last.y, x-last.x)
        else:
            self.theta=0

class Robot:

    def __init__(self):
        # Inicializamos el nodo.
        rospy.init_node('robot_controller', anonymous=True, log_level=debug_level(debug))

        # publicamos la velocidad en el topic /cmd_vel
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.pos_publisher = rospy.Publisher('/rrt_pos_marker', Marker, queue_size=100)

        # suscripcion al topic de odom, para obtener la posicion del robot
        self.pose_subscriber = rospy.Subscriber('/odom', Odometry, self.update_pose)

        # servicio para la comunicacion con el planificador
        self.goal_srv = rospy.Service('pure_pursuit', xygoal, self.pp_callback)

        #inicializamos otras variables
        self.rate = rospy.Rate(10)
        self.pose=Pose()
        self.punto_mas_cercano=Pose()


    def update_pose(self, data):
        """funcion para actualizar la posicion"""
        
        self.pose.x = data.pose.pose.position.x
        self.pose.y = data.pose.pose.position.y
        
        orientation = [data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w]
        (_,_,yaw) = tf.transformations.euler_from_quaternion(orientation)
        
        self.pose.theta = yaw


    def pp_callback(self,req):

        x=req.x
        y=req.y
        self.path=[node(x[0],y[0],None)]
        for i in range(1,len(x)):
            self.path.append(node(x[i],y[i],self.path[i-1]))
        self.move2goal()      
        return True

    def distancia(self, goal):
        return sqrt(pow(goal.x-self.pose.x,2)+pow(goal.y-self.pose.y,2))

    def distancia_recta(self, recta):
        #transformamos a los ejes del robot
        x=recta.x-self.pose.x
        y=recta.y-self.pose.y
        m=atan(recta.theta) #pendiente de la recta
        b=y-m*x #corte al eje x de la recta
        self.punto_mas_cercano.x=-b/(m+1/m) #x del punto mas cercano al robot
        self.punto_mas_cercano.y=m*self.punto_mas_cercano.x+b
        distancia_recta=sqrt(pow(self.punto_mas_cercano.x,2)+pow(self.punto_mas_cercano.y,2)) #este numero es siempre positivo, cuando queramos girar hacia el otro
        return distancia_recta

    def find_recta(self):
        objetivo=Point()
        objetivo.x=self.punto_mas_cercano.x
        objetivo.y=self.punto_mas_cercano.y
        angle=atan2(objetivo.y,objetivo.x)
        angle= angle - self.pose.theta
        return angle
        
    def calcular_giro(self,recta):
        a=sqrt(pow(self.punto_mas_cercano.x,2)+pow(self.punto_mas_cercano.y,2))
        d=sqrt(pow(distancia_lookahead,2)-pow(a,2)) # en el if que llama a esta funcion se comprueba que distancia_lookahead>a en magnitud
        objetivo=Point()
        objetivo.x=self.punto_mas_cercano.x+d*cos(recta.theta)
        objetivo.y=self.punto_mas_cercano.y+d*sin(recta.theta)
        objetivo.z=atan2(objetivo.y,objetivo.x)

        #transformamos a los ejes del robot

        distancia_x=distancia_lookahead*cos(self.pose.theta-objetivo.z)
        distancia_y=distancia_lookahead*sin(self.pose.theta-objetivo.z)

        #por geometria

        
        if self.pose.theta-objetivo.z >= 0:
            curbatura= -2*distancia_x/pow(distancia_lookahead,2)
        else:
            curbatura= 2*distancia_x/pow(distancia_lookahead,2) #negativo porque el giro debe ser a la derecha (negativo)

        return curbatura

    def move2goal(self):
        """Moves the robot to the goal."""
        
        vel_msg = Twist()

        self.pos_marker=Marker()
        self.lp=Point() #punto para pintar la posicion
        self.lp.x=self.pose.x
        self.lp.y=self.pose.y
        self.lp.z=0.5
        for pos in self.path: #recorremos todos los puntos
            print("nuevo punto")
            while self.distancia(pos) >= distancia_lookahead: #mientras no lleguemos al punto objetivo con la distancia lookahead
                distancia_recta=self.distancia_recta(pos)
                if distancia_recta > distancia_lookahead:#estamos muy lejos, hay que rectificar, un control proporcional para volver a la recta            
                    angulo=self.find_recta()
                    print(["rectifica", angulo])
                else:
                    angulo=self.calcular_giro(pos)
                    print([angulo])
                
                
                vel_msg.linear.x = velocidad
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                # Angular velocity in the z-axis.
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = angulo

                # Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)

                #imprime la posicion
                self.print_pos()

                # Publish at the desired rate.
                self.rate.sleep()

        # paramos el robot cuando hemos llegado
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    def print_pos(self):
    
        self.pos_marker.header.frame_id = "map"
        self.pos_marker.header.stamp = rospy.Time()
        self.pos_marker.type = Marker.LINE_LIST #check msg info para ver que se refiere a lineas
        self.pos_marker.action = Marker.ADD #0 para add 3 para delete
        self.pos_marker.pose.orientation.w = 1.0
        self.pos_marker.scale.x = 0.08
        self.pos_marker.color.a = 1.0#  Don't forget to set the alpha!
        self.pos_marker.color.r = 0.0
        self.pos_marker.color.g = 0.0
        self.pos_marker.color.b = 1.0
        p2=Point()
        p2.x=self.pose.x
        p2.y=self.pose.y
        p2.z=0.5
        #print(["point",p1.x,p1.y,p2.x,p2.y])
        self.pos_marker.points.append(self.lp)
        self.pos_marker.points.append(p2)
        self.pos_publisher.publish(self.pos_marker)
        self.lp=p2
        self.rate.sleep()


if __name__ == '__main__':
    try:
        x = Robot()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
