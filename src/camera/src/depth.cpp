#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <camera/Depth.h>
#include <librealsense2/rs.hpp>

int main(int argc, char **argv){
  ros::init(argc, argv, "depth_stream");
  ros::NodeHandle n;

  // Create a publisher node
  ros::Publisher depth_pub = n.advertise<camera::Depth>("depth_frames", 1000);

  // Instantiate an instance of a message
  camera::Depth msg;
  // Create a Pipeline - this serves as a top-level API for streaming and processing frames
  rs2::pipeline p;
  // Configure and start the pipeline
  rs2::config config;
  config.enable_stream(RS2_STREAM_DEPTH);
  p.start(config);
  while (true)
  {
      // Block program until frames arrive
      rs2::frameset frames = p.wait_for_frames();

      // Try to get a frame of a depth image
      rs2::depth_frame depth = frames.get_depth_frame();

      // Get the depth frame's dimensions
      float width = depth.get_width();
      float height = depth.get_height();

      // Query the distance from the camera to the object in the center of the image
      float dist_to_center = depth.get_distance(width / 2, height / 2);
      msg.center_depth = dist_to_center;
      // msg.left_depth = ;
      // msg.right_depth = ;
      // Print the distance

      // Publish the message
      depth_pub.publish(msg)
      // ROS_INFO("The camera is facing an object %f meters away \n", dist_to_center);
  }
  return 0;
}
