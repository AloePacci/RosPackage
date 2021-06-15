// Generated by gencpp from file stage/xygoalResponse.msg
// DO NOT EDIT!


#ifndef STAGE_MESSAGE_XYGOALRESPONSE_H
#define STAGE_MESSAGE_XYGOALRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace stage
{
template <class ContainerAllocator>
struct xygoalResponse_
{
  typedef xygoalResponse_<ContainerAllocator> Type;

  xygoalResponse_()
    : reach(false)  {
    }
  xygoalResponse_(const ContainerAllocator& _alloc)
    : reach(false)  {
  (void)_alloc;
    }



   typedef uint8_t _reach_type;
  _reach_type reach;





  typedef boost::shared_ptr< ::stage::xygoalResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::stage::xygoalResponse_<ContainerAllocator> const> ConstPtr;

}; // struct xygoalResponse_

typedef ::stage::xygoalResponse_<std::allocator<void> > xygoalResponse;

typedef boost::shared_ptr< ::stage::xygoalResponse > xygoalResponsePtr;
typedef boost::shared_ptr< ::stage::xygoalResponse const> xygoalResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::stage::xygoalResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::stage::xygoalResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::stage::xygoalResponse_<ContainerAllocator1> & lhs, const ::stage::xygoalResponse_<ContainerAllocator2> & rhs)
{
  return lhs.reach == rhs.reach;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::stage::xygoalResponse_<ContainerAllocator1> & lhs, const ::stage::xygoalResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace stage

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::stage::xygoalResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::stage::xygoalResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::stage::xygoalResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::stage::xygoalResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stage::xygoalResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stage::xygoalResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::stage::xygoalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e28478de0c42bf45c139fda1fb68c47f";
  }

  static const char* value(const ::stage::xygoalResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe28478de0c42bf45ULL;
  static const uint64_t static_value2 = 0xc139fda1fb68c47fULL;
};

template<class ContainerAllocator>
struct DataType< ::stage::xygoalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "stage/xygoalResponse";
  }

  static const char* value(const ::stage::xygoalResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::stage::xygoalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool reach\n"
;
  }

  static const char* value(const ::stage::xygoalResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::stage::xygoalResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.reach);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct xygoalResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::stage::xygoalResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::stage::xygoalResponse_<ContainerAllocator>& v)
  {
    s << indent << "reach: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.reach);
  }
};

} // namespace message_operations
} // namespace ros

#endif // STAGE_MESSAGE_XYGOALRESPONSE_H