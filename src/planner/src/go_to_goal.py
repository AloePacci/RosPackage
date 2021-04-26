#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
from math import pow, atan2, sqrt
import tf.transformations
from planner.srv import GoTo

pi=3.141592653589793

class pid:
    def __init__(self, kp, ki, kd):
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.dererr=0.0
        self.interr=0.0

    def derivative(self, error):
        a=self.dererr
        self.dererr=error
        return self.kd*(error-a)

    def integral(self, error):
        self.interr+=error
        return self.interr * self.ki

    def proportional(self, error):
        return error*self.kp

    def PD(self, error):
        return self.proportional(error)+self.derivative(error)
    
    def PI(self, error):
        return self.proportional(error)+self.integral(error)

    def PID(self, error):
        return self.proportional(error)+self.integral(error)+self.derivative(error)

class Robot:

    def __init__(self):
        # Creates a node with name 'robot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('robot_controller', anonymous=True)

        # Publisher which will publish to the topic '/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/odom'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/odom',
                                                Odometry, self.update_pose)
        self.angularcontroller=pid(4.0,0.0,0.0)
        self.positioncontroller=pid(0.5,0.01,0.01)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

        self.goal_srv = rospy.Service('goto', GoTo, self.goto_callback)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        
        self.pose.x = round(data.pose.pose.position.x, 4)
        self.pose.y = round(data.pose.pose.position.y, 4)
        
        orientation = [data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w]
        (_,_,yaw) = tf.transformations.euler_from_quaternion(orientation)
        
        self.pose.theta = yaw

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose):
        return self.positioncontroller.PID(self.euclidean_distance(goal_pose))

    def steering_angle(self, goal_pose):
        angledif=atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta
        if angledif>pi:
            angledif-=2*pi
        if angledif<-pi:
            angledif+=2*pi
        return angledif

    def angular_vel(self, goal_pose):
        return self.angularcontroller.PID(self.steering_angle(goal_pose))

    def goto_callback(self,req):

        goal_pose = Pose()
        goal_pose.x = req.x-9.5
        goal_pose.y = 7.5-req.y

        print('Going to goal: ' + str(goal_pose.x) + ',' + str(goal_pose.y))    
         
        self.move2goal(goal_pose, req.dist_tolerance)

        return True

    def move2goal(self, goal_pose, distance_tolerance):
        """Moves the robot to the goal."""
        
        vel_msg = Twist()

        while self.euclidean_distance(goal_pose) >= distance_tolerance:

            # Porportional controller.
            # https://en.wikipedia.org/wiki/Proportional_control

            # Linear velocity in the x-axis.
            if abs(self.steering_angle(goal_pose))<0.44:  #aprox 25 degrees
                vel_msg.linear.x = self.linear_vel(goal_pose)
            else:
                vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        x = Robot()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
