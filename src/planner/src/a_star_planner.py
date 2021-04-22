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
        start_cell[0]-=0.5
        start_cell[1]-=0.5
        path.append(start_cell)

        apoint=[int(start_cell[0]), int(start_cell[1])]
        ######################
        # TODO: Implement A* #
        ######################
        g=np.ones((self.height, self.width))*(-1)  #npasos
        px=np.ones((self.height, self.width))*(-1)   #celda padre
        py=np.ones((self.height, self.width))*(-1)  #celda padre
        print(apoint)
        seen=np.zeros((self.height, self.width))
        seen[apoint[0], apoint[1]]=1 #we mark start point as seen
        counter=0 #number of steps
        while apoint != goal_cell:
            auxup=[apoint[0]-1,apoint[1]]
            auxright=[apoint[0],apoint[1]+1]
            auxdown=[apoint[0]+1,apoint[1]]
            auxleft=[apoint[0],apoint[1]-1]
            h=round(abs(goal_cell[0]-apoint[0])+abs(goal_cell[1]-apoint[1]))
            g[apoint[0],apoint[1]]=counter
            if self.map[auxup[0],auxup[1]]==1:
                # este punto esta ocupado
                seen[auxup[0],auxup[1]]=1
            else:
                if (g[auxup[0],auxup[1]]!=-1) & (g[auxup[0],auxup[1]]<counter):
                    #ya hemos pasado por este punto
                    a=0
                else:
                    if round(abs(goal_cell[0]-auxup[0])+abs(goal_cell[1]-auxup[1]))<h:
                        a=0
                        #estamos mas cerca del destino
            break

        ######################
        # End A*             #
        ######################
        path.append(goal_cell)
        # Print path
        x = []
        y = []
        
        for point in path:
            x.append(point[1])
            y.append(point[0])
        
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

        path2=[ [3, 2, 5], [12, 11, 11] ]
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
