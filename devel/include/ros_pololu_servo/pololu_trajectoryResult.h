// Generated by gencpp from file ros_pololu_servo/pololu_trajectoryResult.msg
// DO NOT EDIT!


#ifndef ROS_POLOLU_SERVO_MESSAGE_POLOLU_TRAJECTORYRESULT_H
#define ROS_POLOLU_SERVO_MESSAGE_POLOLU_TRAJECTORYRESULT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ros_pololu_servo
{
template <class ContainerAllocator>
struct pololu_trajectoryResult_
{
  typedef pololu_trajectoryResult_<ContainerAllocator> Type;

  pololu_trajectoryResult_()
    : success(false)  {
    }
  pololu_trajectoryResult_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> const> ConstPtr;

}; // struct pololu_trajectoryResult_

typedef ::ros_pololu_servo::pololu_trajectoryResult_<std::allocator<void> > pololu_trajectoryResult;

typedef boost::shared_ptr< ::ros_pololu_servo::pololu_trajectoryResult > pololu_trajectoryResultPtr;
typedef boost::shared_ptr< ::ros_pololu_servo::pololu_trajectoryResult const> pololu_trajectoryResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ros_pololu_servo

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsMessage': True, 'IsFixedSize': True, 'HasHeader': False}
// {'ros_pololu_servo': ['/home/karan/advanced_robotics_ws/src/ros_pololu/src/ros_pololu_servo/msg', '/home/karan/advanced_robotics_ws/devel/share/ros_pololu_servo/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'trajectory_msgs': ['/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsMessage< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_pololu_servo/pololu_trajectoryResult";
  }

  static const char* value(const ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Define the result\n\
bool success\n\
";
  }

  static const char* value(const ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct pololu_trajectoryResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_pololu_servo::pololu_trajectoryResult_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_POLOLU_SERVO_MESSAGE_POLOLU_TRAJECTORYRESULT_H
