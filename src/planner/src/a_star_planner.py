#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
import tf.transformations
import numpy as np
import matplotlib.pyplot as plt
from planner.srv import GoTo


    


class Planner:

    def __init__(self):
        
        # A subscriber to the topic '/odom'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/odom',
                                                Odometry, self.update_pose)

        self.pose = Pose()
        # Load map
        self.map = np.genfromtxt('/home/aloepacci/RosPackage/src/planner/worlds/map.csv', delimiter=',')
        self.height = self.map.shape[0]
        self.width = self.map.shape[1]
        self.resolution = 1
        
        # Print map
        image = np.flipud(self.map)
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
        start_cell[0]=int(round(start_cell[0]))
        start_cell[1]=int(round(start_cell[1]))

        pointpos=start_cell

        #declarations
        self.cell_g=np.ones((self.height, self.width))*(-1)  #npasos
        self.cell_h=np.ones((self.height, self.width))*(-1)  #distancia
        self.cell_px=np.ones((self.height, self.width))*(-1)   #celda padre
        self.cell_py=np.ones((self.height, self.width))*(-1)  #celda padre
        self.cell_seen=np.zeros((self.height, self.width))
        step=0
        x=np.zeros(100)
        y=np.zeros(100)
      

        #start point
        self.cell_seen[start_cell[0], start_cell[1]]=1 #we mark start point as seen
        self.cell_px[start_cell[0], start_cell[1]]=start_cell[0]   #celda padre
        self.cell_py[start_cell[0], start_cell[1]]=start_cell[1]   #celda padre
        self.cell_g[start_cell[0], start_cell[1]]=step
        x[0]=start_cell[1]
        y[0]=start_cell[0]

        counter2=0
        while ((pointpos[1] != goal_cell[1]) or (pointpos[0] != goal_cell[0])):
            step=step+1
            reiterate=True
            #elegimos una celda que no sea pared como primera candidata.
            if self.map[pointpos[0]+1,pointpos[1]]==0:
                nextcell=[pointpos[0]+1,pointpos[1]] #por defecto va a ser arriba
            else:
                if self.map[pointpos[0],pointpos[1]+1]==0:
                    nextcell=[pointpos[0],pointpos[1]+1] #derecha
                else:
                    if self.map[pointpos[0]-1,pointpos[1]]==0:
                        nextcell=[pointpos[0]-1,pointpos[1]] #abajo
                    else:
                        nextcell=[pointpos[0],pointpos[1]-1] #izquierda, este es el peor de los casos. consideramos que no podemos estar en un lugar sin movimientos.
            
            while reiterate==True: # mientras no hayamos encontrado la mejor celda

                #distancia inicial
                h=abs(nextcell[0]-goal_cell[0])+abs(nextcell[1]-goal_cell[1])
                
                #buscamos una celda que sea mejor
                if self.map[pointpos[0]+1,pointpos[1]]==0 and (abs(pointpos[0]+1-goal_cell[0])+abs(pointpos[1]-goal_cell[1]))<h:#arriba
                    nextcell=[pointpos[0]+1,pointpos[1]]
                else:
                    if self.map[pointpos[0],pointpos[1]+1]==0 and (abs(pointpos[0]-goal_cell[0])+abs(pointpos[1]+1-goal_cell[1]))<h:#derecha
                        nextcell=[pointpos[0],pointpos[1]+1] #derecha
                    else:
                        if self.map[pointpos[0]-1,pointpos[1]]==0 and (abs(pointpos[0]-1-goal_cell[0])+abs(pointpos[1]-goal_cell[1]))<h:#abajo
                            nextcell=[pointpos[0]-1,pointpos[1]] #abajo
                        else:
                            if self.map[pointpos[0],pointpos[1]-1]==0 and (abs(pointpos[0]-goal_cell[0])+abs(pointpos[1]-1-goal_cell[1]))<h:#izquierda
                                nextcell=[pointpos[0],pointpos[1]-1] #izquierda
                            else:
                                reiterate=False #parece ser la celda que promete estar mas cerca del objetivo
                
                if self.cell_seen[nextcell[0], nextcell[1]]==1:     #esta celda ya la hemos visto
                    reiterate=True

            self.cell_seen[nextcell[0], nextcell[1]]=1 #marcamos la celda como vista

            x[step]=nextcell[1]  #la aniadimos a la lista
            y[step]=nextcell[0]
            pointpos=nextcell
            print(pointpos)
        print(goal_cell)


        ######################
        # End A*             #
        ######################
        
        # Print path

        
        #for point in path:
        path.append(goal_cell)
        
        image = np.flipud(self.map)
        plt.figure()
        plt.imshow(image, cmap=plt.get_cmap('binary'))
        plt.plot(x,y,'ro-', linewidth=2, markersize=5)
        plt.show()
        
        return path


    def goto(self):
        """Moves the robot to the goal."""

        goal_pose = Pose()
        # Get the input from the user.
        # Test with -0.5,3.5 meters
        while True:
            goal_pose.x = int(input("Set your x goal: "))
            goal_pose.y = int(input("Set your y goal: "))
            if self.map[goal_pose.y,goal_pose.x] == 1:
                print("esta celda esta ocupada")
            else:
                break

        current_cell = [8-self.pose.y,10+self.pose.x]
        goal_cell = [goal_pose.y,goal_pose.x]

        path = self.compute_path(current_cell,goal_cell)

        path2=[ [3], [12] ]
        counter=0
        state=False
        for point in path2:
            rospy.wait_for_service('goto')
            try:
                Goto_service = rospy.ServiceProxy('goto', GoTo)
                resp1 = Goto_service(path2[0][counter], path2[1][counter], 0.15)
                while state==False:
                    state=resp1.success
                counter+=1
                
            except rospy.ServiceException as e:
                print("Service call failed: %s"%e)
            pass
        
if __name__ == '__main__':
    try:
        rospy.init_node('robot_planner', anonymous=True)

        x = Planner()
        x.goto()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
