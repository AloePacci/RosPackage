#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
import tf.transformations
import numpy as np
import matplotlib.pyplot as plt
from planner.srv import GoTo
from math import sqrt, pow


distancia_mode=-1   #"'0' taxista" o '1' "euclidea"

class Cell:
    def __init__(self,casilla, padre, g, f):
        self.casilla=casilla
        self.padre=padre
        self.g=g
        self.f=f

class Planner:

    def __init__(self):
        
        # A subscriber to the topic '/odom'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/odom',
                                                Odometry, self.update_pose)

        self.pose = Pose()
        # Load map
        self.map = np.genfromtxt('/home/aloepacci/RosPackage/src/planner/worlds/map.csv', sep=',')
        self.height = self.map.shape[0]
        self.width = self.map.shape[1]
        self.resolution = 1
        
        # Print map
        #image = np.flipud(self.map)
        #plt.figure()
        #plt.imshow(image, cmap=plt.get_cmap('binary'))
        #plt.show()

        
    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        
        self.pose.x = round(data.pose.pose.position.x, 4)
        self.pose.y = round(data.pose.pose.position.y, 4)
        
        orientation = [data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w]
        (_,_,yaw) = tf.transformations.euler_from_quaternion(orientation)
        
        self.pose.theta = yaw

    def compute_path(self, start_cell, goal_cell):
        """Compute path."""
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
        """Moves the robot to the goal."""

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
            print("Hemos llegado!")
        
if __name__ == '__main__':
    try:
        rospy.init_node('robot_planner', anonymous=True)
        while distancia_mode!=0 and distancia_mode!=1:
            distancia_mode=input("introduzca 1 para distancia euclidea, 0 para distancia taxista: ")
        x = Planner()
        x.goto()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
