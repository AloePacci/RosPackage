// Generated by gencpp from file turtle_pid_control/xygoal.msg
// DO NOT EDIT!


#ifndef TURTLE_PID_CONTROL_MESSAGE_XYGOAL_H
#define TURTLE_PID_CONTROL_MESSAGE_XYGOAL_H

#include <ros/service_traits.h>


#include <turtle_pid_control/xygoalRequest.h>
#include <turtle_pid_control/xygoalResponse.h>


namespace turtle_pid_control
{

struct xygoal
{

typedef xygoalRequest Request;
typedef xygoalResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct xygoal
} // namespace turtle_pid_control


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::turtle_pid_control::xygoal > {
  static const char* value()
  {
    return "d19ef5ce3bf2af44ecc2f565e73d87ee";
  }

  static const char* value(const ::turtle_pid_control::xygoal&) { return value(); }
};

template<>
struct DataType< ::turtle_pid_control::xygoal > {
  static const char* value()
  {
    return "turtle_pid_control/xygoal";
  }

  static const char* value(const ::turtle_pid_control::xygoal&) { return value(); }
};


// service_traits::MD5Sum< ::turtle_pid_control::xygoalRequest> should match
// service_traits::MD5Sum< ::turtle_pid_control::xygoal >
template<>
struct MD5Sum< ::turtle_pid_control::xygoalRequest>
{
  static const char* value()
  {
    return MD5Sum< ::turtle_pid_control::xygoal >::value();
  }
  static const char* value(const ::turtle_pid_control::xygoalRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::turtle_pid_control::xygoalRequest> should match
// service_traits::DataType< ::turtle_pid_control::xygoal >
template<>
struct DataType< ::turtle_pid_control::xygoalRequest>
{
  static const char* value()
  {
    return DataType< ::turtle_pid_control::xygoal >::value();
  }
  static const char* value(const ::turtle_pid_control::xygoalRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::turtle_pid_control::xygoalResponse> should match
// service_traits::MD5Sum< ::turtle_pid_control::xygoal >
template<>
struct MD5Sum< ::turtle_pid_control::xygoalResponse>
{
  static const char* value()
  {
    return MD5Sum< ::turtle_pid_control::xygoal >::value();
  }
  static const char* value(const ::turtle_pid_control::xygoalResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::turtle_pid_control::xygoalResponse> should match
// service_traits::DataType< ::turtle_pid_control::xygoal >
template<>
struct DataType< ::turtle_pid_control::xygoalResponse>
{
  static const char* value()
  {
    return DataType< ::turtle_pid_control::xygoal >::value();
  }
  static const char* value(const ::turtle_pid_control::xygoalResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // TURTLE_PID_CONTROL_MESSAGE_XYGOAL_H
