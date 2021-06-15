#include "ros/ros.h"
#include "stage/xygoal.h"
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
#include "math.h"


geometry_msgs::Twist command;
turtlesim::Pose data;

void read_pose(const turtlesim::Pose&  pos)
{
  data.x=pos.x;
  data.y=pos.y;
  data.theta=pos.theta;
}

bool go_to_destination(stage::xygoal::Request  &req, stage::xygoal::Response &res)
{
  float tol=1;
  float distance, angle=atan2(req.x-data.x,req.y-data.y);
  float kp=0.1,ka=3;
   ros::NodeHandle n;
  command.linear.y=0;
  command.linear.z=0;
  command.angular.x=0;
  command.angular.y=0;
  ros::Publisher command_sender = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1000);
  ros::Subscriber position_updater = n.subscribe("/turtle1/pose", 1000, read_pose);
  ros::spinOnce();
  ROS_INFO("actual pos: x=%f, y=%f, theta=%f", data.x, data.y, data.theta);
  ROS_INFO("goal pos: x=%f, y=%f, theta=%f", req.x, req.y, angle);
  do{
      distance=sqrt((req.x-data.x)*(req.x-data.x)+(req.y-data.y)*(req.y-data.y));
      angle=atan2(req.x-data.x,req.y-data.y)-data.theta;
      command.linear.x=kp*distance;
      command.angular.z=ka*(angle);
      command_sender.publish(command);
      ros::spinOnce();
  }while(distance>tol);
    ROS_INFO("reached goal");
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "controlador");
  ros::NodeHandle n;
  ros::ServiceServer service = n.advertiseService("controlador", go_to_destination);

  ROS_INFO("Ready to drive");
  ros::spin();

  return 0;
}