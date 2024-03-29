// Generated by gencpp from file GUI/Num.msg
// DO NOT EDIT!


#ifndef GUI_MESSAGE_NUM_H
#define GUI_MESSAGE_NUM_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace GUI
{
template <class ContainerAllocator>
struct Num_
{
  typedef Num_<ContainerAllocator> Type;

  Num_()
    : circlesNo(0)
    , trianglesNo(0)
    , linesNo(0)
    , squaresNo(0)  {
    }
  Num_(const ContainerAllocator& _alloc)
    : circlesNo(0)
    , trianglesNo(0)
    , linesNo(0)
    , squaresNo(0)  {
  (void)_alloc;
    }



   typedef int64_t _circlesNo_type;
  _circlesNo_type circlesNo;

   typedef int64_t _trianglesNo_type;
  _trianglesNo_type trianglesNo;

   typedef int64_t _linesNo_type;
  _linesNo_type linesNo;

   typedef int64_t _squaresNo_type;
  _squaresNo_type squaresNo;





  typedef boost::shared_ptr< ::GUI::Num_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::GUI::Num_<ContainerAllocator> const> ConstPtr;

}; // struct Num_

typedef ::GUI::Num_<std::allocator<void> > Num;

typedef boost::shared_ptr< ::GUI::Num > NumPtr;
typedef boost::shared_ptr< ::GUI::Num const> NumConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::GUI::Num_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::GUI::Num_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace GUI

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'GUI': ['/home/mahfouz/fuckin_ws/src/GUI/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::GUI::Num_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::GUI::Num_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::GUI::Num_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::GUI::Num_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::GUI::Num_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::GUI::Num_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::GUI::Num_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cc4fa4ab5eb670e25a1c738431aed253";
  }

  static const char* value(const ::GUI::Num_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xcc4fa4ab5eb670e2ULL;
  static const uint64_t static_value2 = 0x5a1c738431aed253ULL;
};

template<class ContainerAllocator>
struct DataType< ::GUI::Num_<ContainerAllocator> >
{
  static const char* value()
  {
    return "GUI/Num";
  }

  static const char* value(const ::GUI::Num_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::GUI::Num_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 circlesNo\n\
int64 trianglesNo\n\
int64 linesNo\n\
int64 squaresNo\n\
";
  }

  static const char* value(const ::GUI::Num_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::GUI::Num_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.circlesNo);
      stream.next(m.trianglesNo);
      stream.next(m.linesNo);
      stream.next(m.squaresNo);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Num_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::GUI::Num_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::GUI::Num_<ContainerAllocator>& v)
  {
    s << indent << "circlesNo: ";
    Printer<int64_t>::stream(s, indent + "  ", v.circlesNo);
    s << indent << "trianglesNo: ";
    Printer<int64_t>::stream(s, indent + "  ", v.trianglesNo);
    s << indent << "linesNo: ";
    Printer<int64_t>::stream(s, indent + "  ", v.linesNo);
    s << indent << "squaresNo: ";
    Printer<int64_t>::stream(s, indent + "  ", v.squaresNo);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GUI_MESSAGE_NUM_H
