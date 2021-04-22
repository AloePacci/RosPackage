#include "ros/ros.h"
#include "turtle_pid_control/xygoal.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "turtledriver");
  if (argc != 3)
  {
    ROS_INFO("usage: add_two_ints_client X Y");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<turtle_pid_control::xygoal>("turtle_driver");
  turtle_pid_control::xygoal srv;
  srv.request.x = atof(argv[1]);
  srv.request.y = atof(argv[2]);
  if (client.call(srv))
  {
    ROS_INFO("we have reached destination");
  }
  else
  {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }

  return 0;
}