#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry, OccupancyGrid
import tf.transformations
import numpy as np
import matplotlib.pyplot as plt
from stage.srv import xygoal
from math import sqrt, pow





class Rama:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Planner:

    def __init__(self):
        
        # nos suscribimos a '/odom' para obtener la posicion del robot
        self.pose_subscriber = rospy.Subscriber('/odom', Odometry, self.update_pose)                                     
        self.pose = Pose()

        # obtenemos datos del mapa
        self.map_subscriber = rospy.Subscriber('/map', OccupancyGrid, self.map_update)

        
        
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
        self.resolution = data.info.resolution
        self.map_origin = [data.info.origin.position.x, data.info.origin.position.y]
        self.map = np.zeros((self.height,self.width))
        counter=0
        counter2=0
        for i in data.data:
            if i==0:
                self.map[counter][counter2]=0   #pixel libre
            else:
                self.map[counter][counter2]=1   #pixel ocupado
            counter+=1
            if counter == self.width:
                counter=0
                counter2+=1             

    def dist(init,end):
        """vamos a trabajar con la distancia euclidea"""
        return sqrt(pow(init[0]-end[0],2)+pow(init[1]-end[1],2))

    """def compute_path(self, start_cell, goal_cell):
        #Compute path.
        path = []
        start_cell[0]=int(round(start_cell[0]-0.5)) #vamos a suponer que la primera casilla es la 0, tal y como se indica en el mapa- por los valores que vemos en el
        start_cell[1]=int(round(start_cell[1]-0.5)) #echo odom, necesitamos rectificar un ofset de -0.5

        pointpos=start_cell

        #declarations
        self.openlist=[]
        self.closedlist=[]
      

        #start point paso 0
        if distancia_mode==1:
            self.openlist.append(Cell([start_cell[0], start_cell[1]],[start_cell[0], start_cell[1]],0,sqrt(pow(pointpos[0]+1-goal_cell[0],2)+pow(pointpos[1]-goal_cell[1],2))))
        else:
                        self.openlist.append(Cell([start_cell[0], start_cell[1]],[start_cell[0], start_cell[1]],0,abs(pointpos[0]+1-goal_cell[0])+abs(pointpos[1]-goal_cell[1])))
        while len(self.openlist)!=0: #mientras la lista no este vacia
            candidata=self.openlist.pop(0)
            self.closedlist.append(candidata)
            if candidata.casilla == goal_cell: #si hemos llegado, salimos
                break
            neighbour=[[candidata.casilla[0]+1, candidata.casilla[1]], [candidata.casilla[0], candidata.casilla[1]+1], [candidata.casilla[0]-1, candidata.casilla[1]], [candidata.casilla[0], candidata.casilla[1]-1]]

            for x in range(4):
                pertenece=False
                if self.map[neighbour[x][0], neighbour[x][1]]==0:#no es una pared
                    for i in self.openlist:
                        if ([neighbour[x][0], neighbour[x][1]] == i.casilla): #pertenece a la lista abierta
                            pertenece=True
                            if(i.g<candidata.g-1):
                                candidata=self.openlist.pop()
                                candidata.padre=i.casilla
                                candidata.g=i.g+1
                                self.openlist.append(candidata)

                    for i in self.closedlist:
                        if ([neighbour[x][0], neighbour[x][1]] == i.casilla): #pertenece a la lista cerrada
                            pertenece=True
                            if(i.g<candidata.g-1):
                                candidata=self.closedlist.pop()
                                candidata.padre=i.casilla
                                candidata.g=i.g+1
                                self.closedlist.append(candidata)
                    
                    if pertenece==False: #no pertenece a una lista
                        if distancia_mode==1:
                            self.openlist.append(Cell([neighbour[x][0], neighbour[x][1]],[candidata.casilla[0], candidata.casilla[1]],candidata.g+1,pow(neighbour[x][0]-goal_cell[0],2)+pow(neighbour[x][1]-goal_cell[1],2)))
                        else:
                            self.openlist.append(Cell([neighbour[x][0], neighbour[x][1]],[candidata.casilla[0], candidata.casilla[1]],candidata.g+1,abs(neighbour[x][0]-goal_cell[0])+abs(neighbour[x][1]-goal_cell[1])))

            self.openlist.sort(key=lambda Cell : Cell.f)#reordenamos la lista
        
        path2=[]
        if len(self.openlist)==0 and self.closedlist[0].casilla!=goal_cell: #hemos revisado todos los puntos
            print("no hemos encontrado un camino")
        else:
            parent=goal_cell
            while parent != start_cell: #hasta que no tengamos el punto inicial
                casilla=self.closedlist.pop()
                if casilla.casilla == parent: #buscamos su padre
                    path2.append(casilla.padre)
                    parent=casilla.padre

        path2.reverse() #queremos el orden contrario, del principio a fin
        for i in path2:#lo asignamos a la lista
            path.append(i)
        path.append(goal_cell)#asignamos el punto final

        # Print path
        
        x=[]
        y=[]
        for i in path:
            x.append(i[0])
            y.append(i[1])
        
        
        image = np.flipud(self.map)
        plt.figure()
        plt.imshow(image, cmap=plt.get_cmap('binary'))
        plt.plot(y,x,'ro-', linewidth=2, markersize=5)
        plt.show()
        
        return path


    def goto(self):
        #Moves the robot to the goal.

        goal_pose = Pose()

        while True:
            while True:
                goal_pose.x = int(input("Set your x goal: "))
                goal_pose.y = int(input("Set your y goal: ")) #TODO add una secuencia de volver a pedir si la posicion esta fuera del rango del mapa, indicando dimensiones
                if self.map[goal_pose.y,goal_pose.x] == 1:
                    print("esta celda esta ocupada")
                else:
                    break

            current_cell = [8-self.pose.y,10+self.pose.x]
            goal_cell = [goal_pose.y,goal_pose.x]

            path = self.compute_path(current_cell,goal_cell)

            state=False
            for point in path:
                rospy.wait_for_service('goto')
                try:
                    Goto_service = rospy.ServiceProxy('goto', GoTo)
                    resp1 = Goto_service(point[1], point[0], 0.15)
                    while state==False:
                        state=resp1.success

                    
                except rospy.ServiceException as e:
                    print("Service call failed: %s"%e)
                pass
            print("Hemos llegado!")"""
        
if __name__ == '__main__':
    try:
        rospy.init_node('robot_planner', anonymous=True)
        x = Planner()
        #x.goto()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
