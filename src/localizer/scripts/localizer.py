#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose as PoseRobot
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseArray,Pose
import tf.transformations
import numpy as np
import random
from math import sqrt,exp
import copy

class Particle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0


class ParticleFilter:

    def __init__(self):
        
        # A subscriber to the topic '/base_pose_ground_truth'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/base_pose_ground_truth',
                                                Odometry, self.update_pose)

        # A publisher to the topic 'particles' to publish the cloud of particles
        self.particles_publisher = rospy.Publisher('particles', PoseArray, queue_size = 1)

        self.pose = PoseRobot()
        self.pose_prev = PoseRobot()
        self.pose_received = False

        self.num_particles = 1000
        self.particles = []
        self.weights = []

        self.dist_noise =0.1
        self.ang_noise = 0.1
        self.sense_noise = 1.5

        self.landmarks  = [[-3.5, 1.5], [3.5, 1.5]]

        self.x_min = -10.0
        self.x_max = 10.0
        self.y_min = -7.5
        self.y_max = 7.5
        self.theta_min = -np.pi
        self.theta_max = np.pi 

        self.initialize()

       
    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        
        self.pose.x = round(data.pose.pose.position.x, 4)
        self.pose.y = round(data.pose.pose.position.y, 4)
        
        orientation = [data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w]
        (_,_,yaw) = tf.transformations.euler_from_quaternion(orientation)
        
        self.pose.theta = yaw

        if not self.pose_received:
            
            self.pose_prev = copy.deepcopy(self.pose)
            self.pose_received = True


    def initialize(self):
        """Function to initialize particles in filter."""

        self.particles = []

        for _ in range(self.num_particles):
            p = Particle()
            weight = 0.0

            p.x=self.x_min+random.random()*(self.x_max-self.x_min)
            p.y=self.y_min+random.random()*(self.y_max-self.y_min)
            p.theta=random.random()*(self.theta_max-self.theta_min)
            
            self.particles.append(p)
            self.weights.append(weight)

    def check_robot_motion(self):
        """Function to determine if robot moved enough to update filter."""

        if not self.pose_received:
            return False

        # Compute movement increment from last time
        self.delta_x = self.pose.x - self.pose_prev.x
        self.delta_y = self.pose.y - self.pose_prev.y

        delta_ang1 = self.pose.theta - self.pose_prev.theta
        delta_ang2 = 2*np.pi - abs(delta_ang1)
        if delta_ang1 > 0:
            delta_ang2 *= -1.0
        if abs(delta_ang1) < abs(delta_ang2):
            self.delta_theta = delta_ang1
        else:
            self.delta_theta = delta_ang2

        # Predict only if the robot moved enough
        if abs(self.delta_x) > 0.2 or abs(self.delta_y) > 0.2 or abs(self.delta_theta) > np.pi/6.0:
            return True
        else:
            return False


    def sense(self):
        """Function to generate sensor observation from measuring distange to landmarks."""

        Z = []
        for i in range(len(self.landmarks)):
            dist = sqrt((self.pose.x - self.landmarks[i][0]) ** 2 + (self.pose.y - self.landmarks[i][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            Z.append(dist)
        return Z


    def predict(self):
        """Function to predict particles according to robot motion."""

        for p in self.particles:

            p.x+=self.delta_x+random.gauss(0.0, self.dist_noise)
            p.y+=self.delta_y+random.gauss(0.0, self.dist_noise)
            p.theta+=self.delta_theta+random.gauss(0.0, self.ang_noise)


        self.pose_prev = copy.deepcopy(self.pose)


    def gaussian(self, mu, sigma, x):
            """ calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma"""
            return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * np.pi * (sigma ** 2))


    def update(self, Z):
        """Function to update particle weights according to the probability of observation Z."""
        """ Z = [d1 d2 ... dn], where di is distance to landmark i. """

        self.weights = []

        for p in self.particles:

            a=sqrt(pow(p.x-self.landmarks[0][0],2)+pow(p.y-self.landmarks[0][1],2))
            b=sqrt(pow(p.x-self.landmarks[1][0],2)+pow(p.y-self.landmarks[1][1],2))
            prob=self.gaussian(Z[0],self.sense_noise,a)*self.gaussian(Z[1],self.sense_noise,b)


            self.weights.append(prob)


    def resample(self):
        """Function to resample particles."""

        p_new = []
        index = int(random.random()*self.num_particles)
        beta = 0
        mw = max(self.weights)

        for i in range(self.num_particles):
            beta += random.random() * 2 * mw
            while beta > self.weights[index]:
                beta -= self.weights[index]
                index = (index + 1)%self.num_particles
            p_new.append(copy.deepcopy(self.particles[index]))

        self.particles = copy.deepcopy(p_new)


    def publish(self):
        """Function to publish the particle cloud for visualization."""
        
        cloud_msg = PoseArray()
        cloud_msg.header.stamp = rospy.get_rostime()
        cloud_msg.header.frame_id = 'map'

        cloud_msg.poses = []
        for i in range(self.num_particles):
            p = Pose()
            p.position.x = self.particles[i].x
            p.position.y = self.particles[i].y
            p.position.z = 0.0

            quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, self.particles[i].theta)
            p.orientation.x = quaternion[0]
            p.orientation.y = quaternion[1]
            p.orientation.z = quaternion[2]
            p.orientation.w = quaternion[3]

            cloud_msg.poses.append(p)

        self.particles_publisher.publish(cloud_msg)

           

if __name__ == '__main__':
    try:
        rospy.init_node('localizer', anonymous=True)

        pf = ParticleFilter()

        r = rospy.Rate(2) # 2hz

        while not rospy.is_shutdown():

            # If robot has moved update filter
            if pf.check_robot_motion():
               
                # Create sensor measurement
                Z = pf.sense()
            
                # Particle Filter steps
                pf.predict()
                pf.update(Z)
                pf.resample()
            
            # Publish particles
            pf.publish()

            r.sleep()

    except rospy.ROSInterruptException:
        pass
