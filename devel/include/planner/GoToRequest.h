// Generated by gencpp from file planner/GoToRequest.msg
// DO NOT EDIT!


#ifndef PLANNER_MESSAGE_GOTOREQUEST_H
#define PLANNER_MESSAGE_GOTOREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace planner
{
template <class ContainerAllocator>
struct GoToRequest_
{
  typedef GoToRequest_<ContainerAllocator> Type;

  GoToRequest_()
    : x(0.0)
    , y(0.0)
    , dist_tolerance(0.0)  {
    }
  GoToRequest_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , dist_tolerance(0.0)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _dist_tolerance_type;
  _dist_tolerance_type dist_tolerance;





  typedef boost::shared_ptr< ::planner::GoToRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::planner::GoToRequest_<ContainerAllocator> const> ConstPtr;

}; // struct GoToRequest_

typedef ::planner::GoToRequest_<std::allocator<void> > GoToRequest;

typedef boost::shared_ptr< ::planner::GoToRequest > GoToRequestPtr;
typedef boost::shared_ptr< ::planner::GoToRequest const> GoToRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::planner::GoToRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::planner::GoToRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::planner::GoToRequest_<ContainerAllocator1> & lhs, const ::planner::GoToRequest_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.dist_tolerance == rhs.dist_tolerance;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::planner::GoToRequest_<ContainerAllocator1> & lhs, const ::planner::GoToRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace planner

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::planner::GoToRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::planner::GoToRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::planner::GoToRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::planner::GoToRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::planner::GoToRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::planner::GoToRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::planner::GoToRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bbe3344c86b0e256ead5b043136b17f8";
  }

  static const char* value(const ::planner::GoToRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbbe3344c86b0e256ULL;
  static const uint64_t static_value2 = 0xead5b043136b17f8ULL;
};

template<class ContainerAllocator>
struct DataType< ::planner::GoToRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "planner/GoToRequest";
  }

  static const char* value(const ::planner::GoToRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::planner::GoToRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x\n"
"float32 y\n"
"float32 dist_tolerance\n"
;
  }

  static const char* value(const ::planner::GoToRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::planner::GoToRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.dist_tolerance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GoToRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::planner::GoToRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::planner::GoToRequest_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "dist_tolerance: ";
    Printer<float>::stream(s, indent + "  ", v.dist_tolerance);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PLANNER_MESSAGE_GOTOREQUEST_H