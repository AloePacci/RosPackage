#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry, OccupancyGrid
from geometry_msgs.msg import PointStamped, Point
from visualization_msgs.msg import Marker
import tf.transformations
import numpy as np
import matplotlib.pyplot as plt
from stage.srv import xygoal
import math
import random

distancia_seguridad=int(rospy.get_param('/rrt_algorithm/distancia_seguridad', 5)) #distancia hasta un obstaculo por la que no trazar un camino (margen de choque) (en pixeles)
max_iterations=int(rospy.get_param("/rrt_algorithm/max_iterations", 10000))
branch_size=int(rospy.get_param('/rrt_algorithm/branch_size', 1)) #size en metros
tolerancia=int(rospy.get_param('/rrt_algorithm/tolerancia', 1)) #size en metros
debug=int(rospy.get_param('/rrt_algorithm/debug_level', 5)) #nivel de debug

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

class Rama:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.camino_x=[]
        self.camino_y=[]
        self.padre=None

class Planner:

    def __init__(self):
        
        # nos suscribimos a '/odom' para obtener la posicion del robot
        self.pose_subscriber = rospy.Subscriber('/odom', Odometry, self.update_pose)                                     
        self.pose = Pose()

        # obtenemos datos del mapa
        self.map_subscriber = rospy.Subscriber('/map', OccupancyGrid, self.map_update)

        #obtenemos posicion a la que dirigirnos
        self.destination_suscriber = rospy.Subscriber('/clicked_point', PointStamped, self.destination_update)

        #publicamos el arbol
        self.tree_publisher = rospy.Publisher('/rrt_gen_marker', Marker, queue_size=100)
        
        
    def update_pose(self, data):
        """Callback function obteniendo datos de la posicion."""
        
        self.pose.x = data.pose.pose.position.x
        self.pose.y = data.pose.pose.position.y
        
        orientation = [data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w]
        (_,_,yaw) = tf.transformations.euler_from_quaternion(orientation)
        
        self.pose.theta = yaw

    def map_update(self, data):
        """Callback function obteniendo datos del mapa, solo se ejecuta una vez al inicio"""
        self.height = data.info.height
        self.width = data.info.width
        self.resolution = data.info.resolution #metro/pixel
        self.map_origin = [data.info.origin.position.x, data.info.origin.position.y]
        self.map = np.zeros((self.height,self.width))

        self.rand_range=[[data.info.origin.position.x+self.width*self.resolution, -self.width*self.resolution-data.info.origin.position.x], [data.info.origin.position.y+self.height*self.resolution, -self.height*self.resolution-data.info.origin.position.y]]
        #print(self.rand_range[0][0]/self.resolution)
        #print(self.rand_range[0][1]/self.resolution)
        counter=0
        counter2=0
        for i in data.data:
            if i!=0:
                self.map[counter2][counter]=1   #pixel ocupado
            counter+=1
            if counter == self.width:
                counter=0
                counter2+=1

        #vamos a aniadir un margen de colision con las paredes para no obtener resultados muy cercanos a las paredes
        for i in range (0,distancia_seguridad):
            counter=1
            counter2=1
            aux=np.zeros((self.height,self.width))
            for k in range(0,(self.height-2)*(self.width-2)):
                if self.map[counter-1][counter2]!=0:
                    aux[counter][counter2]=1
                if self.map[counter][counter2-1]!=0:
                    aux[counter][counter2]=1
                if self.map[counter+1][counter2]!=0:
                    aux[counter][counter2]=1
                if self.map[counter][counter2+1]!=0:
                    aux[counter][counter2]=1

                counter+=1
                if counter == self.height-1:
                    counter=1
                    counter2+=1   
            self.map=aux
        #np.savetxt("foo.csv", self.map, delimiter=",",fmt='%d')
        #image = np.flipud(self.map)
        #plt.figure()
        #plt.imshow(image, cmap=plt.get_cmap('binary'))
        #plt.show()

    def destination_update(self, data):
        self.x_goal=data.point.x
        self.y_goal=data.point.y
        rospy.loginfo("nueva orden, ve a %f %f", self.x_goal, self.y_goal)
        self.found=False #suponemos que no encontramos el punto
        self.plan()

    def dist(self,init,end):
        """vamos a trabajar con la distancia euclidea"""
        return math.sqrt(math.pow(init.x-end.x,2)+math.pow(init.y-end.y,2))

    def plan(self):
        self.comienzo=Rama(self.pose.x,self.pose.y)
        self.final=Rama(self.x_goal,self.y_goal)
        self.Arbol=[self.comienzo] #inicializamos a la posicion inicial
        self.counter_valid=0
        self.counter_invalid=0
        self.n_iteraciones=max_iterations #nos ponemos en el peor caso
        for k in range(0,max_iterations):
            qrand=self.rama_aleatoria()
            if self.extiende(qrand)==1:
                self.n_iteraciones=k
                self.found=True
                self.extiende(Rama(self.x_goal,self.y_goal))#para ir al punto que queremos
                break
        rospy.loginfo("se han creado %d ramas de las que %d son validas y %d invalidas", self.n_iteraciones, self.counter_valid,self.counter_invalid)
        self.actualiza_ramas()
            
        
            

    def rama_aleatoria(self):
        qrand=Rama(
            random.uniform(self.rand_range[0][0],self.rand_range[0][1]),
            random.uniform(self.rand_range[1][0],self.rand_range[1][1])
        )
        return qrand

    def extiende(self, qrand):
        qnear=self.vecinomasproximo(qrand)
        qnew=self.nueva_rama(qnear,qrand)
        
        if self.rama_valida(qnear,qnew):
            self.Arbol.append(qnew)
            self.counter_valid+=1
        else:
            self.counter_invalid+=1
        
        if self.dist(qnear, Rama(self.x_goal, self.y_goal))<tolerancia:
            return True
        return False


        """
        if Nuevaconfiguracion(qrand,qnear,qnew):
            AddadeVertice(arbol,qnew)
            if qnew==qrand:
                return alcanzado
            else:
                return avanzado
        else:
            devuelve rechazado"""

    def rama_valida(self, qnear, qnew):
        
        mapx=round((qnear.x-self.map_origin[0])/self.resolution) #pixeles en el que se encuentra el nodo de la rama
        mapy=round((-(qnear.y+self.map_origin[1]))/self.resolution) 
        destx=round((qnew.x-self.map_origin[0])/self.resolution) #pixeles en el que se encuentra el punto destino de la rama
        desty=round((-(qnew.y+self.map_origin[1]))/self.resolution)

        #queremos buscar si en la linea que los une colisiona con un obstaculo
        theta=math.atan2(desty-mapy,destx-mapx)
        d=int(round(math.sqrt(math.pow(desty-mapy,2)+math.pow(destx-mapx,2)))+1)
        cont=0
        #print([qnear.x-self.map_origin[0],qnear.y+self.map_origin[1],qnew.x,qnew.y])
        #print([mapx, mapy, destx, desty])
        #print(["start check",qnear.x,qnear.y,"map coord",mapx,destx,mapy,desty])
        for i in range(d):
            aux_x=int(round(mapx+cont*math.cos(theta)))
            aux_y=int(round(mapy+cont*math.sin(theta)))
            pixelx=-aux_y
            pixely=aux_x
            if self.map[pixelx][pixely]==1:
                #print(["f",int(round(mapx+cont*math.cos(theta))),int(round(mapy+cont*math.sin(theta))),mapx, mapy, destx, desty])
                return False
            #print([int(round(mapx+cont*math.cos(theta))),int(round(mapy+cont*math.sin(theta)))])
            cont+=1 
        

        return True



    def nueva_rama(self,qnear, qrand):
        qnew=Rama(qnear.x,qnear.y)
        qnew.camino_x=[qnew.x]
        qnew.camino_y=[qnew.y]
        d=self.dist(qnew,qrand)
        theta=math.atan2(qrand.y-qnear.y,qrand.x-qnear.x)

        if d>branch_size:
            d=branch_size
        n_expansiones=int(math.floor(d/self.resolution))

        for j in range(n_expansiones):
            qnew.x+=self.resolution*math.cos(theta)
            qnew.y+=self.resolution*math.sin(theta)
            qnew.camino_x.append(qnew.x)
            qnew.camino_y.append(qnew.y)
        
        d=self.dist(qnew,qrand)
        if d<self.resolution:
            qnew.camino_x.append(qrand.x)
            qnew.camino_y.append(qrand.y)
            qnew.x=qrand.x
            qnew.y=qrand.y
        qnew.padre=qnear
        
        return qnew
        


    def vecinomasproximo(self, qrand):
        dist=[]
        index=0
        for rama in self.Arbol:
            dist.append(self.dist(rama,qrand))
        return self.Arbol[dist.index(min(dist))]

    def actualiza_ramas(self):
        Marker_line=Marker()
        Marker_line.header.frame_id = "map"
        Marker_line.header.stamp = rospy.Time()
        Marker_line.ns = "my_namespace"
        Marker_line.id = 0
        Marker_line.type = Marker.LINE_LIST #check msg info para ver que se refiere a lineas
        Marker_line.action = Marker.ADD #0 para add 3 para delete
        Marker_line.pose.position.x = 1
        Marker_line.pose.position.y = 1
        Marker_line.pose.position.z = 1
        Marker_line.pose.orientation.x = 0.0
        Marker_line.pose.orientation.y = 0.0
        Marker_line.pose.orientation.z = 0.0
        Marker_line.pose.orientation.w = 1.0
        Marker_line.scale.x = 0.2
        Marker_line.scale.y = 0.1
        Marker_line.scale.z = 0.1
        Marker_line.color.a = 1.0#  Don't forget to set the alpha!
        Marker_line.color.r = 0.0
        Marker_line.color.g = 1.0
        Marker_line.color.b = 0.0
        for i in self.Arbol:
            p1=Point()
            p2=Point()
            if i.padre != None:
                p1.x=i.padre.x-1
                p1.y=i.padre.y-1
            else:
                p1.x=i.x-1
                p1.y=i.y-1
            p1.z=0.2
            p2.x=i.x-1
            p2.y=i.y-1
            p2.z=0.5
            #print(["point",p1.x,p1.y,p2.x,p2.y])
            Marker_line.points.append(p1)
            Marker_line.points.append(p2)
        self.tree_publisher.publish(Marker_line)

        
if __name__ == '__main__':
    try:
        rospy.init_node('robot_planner', anonymous=True, log_level=debug_level(debug))
        x = Planner()
        rospy.spin()
        

    except rospy.ROSInterruptException:
        pass
