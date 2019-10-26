#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <camera/Depth.h>
#include <librealsense2/rs.hpp>

float getAverageDepth(rs2::depth_frame depth, float width, float height, int x, int y) {
  float sum = 0;
  int ctr = 0;
  for(int i = y; i < y + height; i++) {
    for (int j = x; j < x + width; j++) {
      float depth_val = depth.get_distance(x, y);
      if (depth_val > 0) {
        ctr += 1;
        sum += depth_val;
      }
    }
  }
  if (ctr == 0) {
    return 0;
  }
  return (sum / ctr);
}

float* getCorners(float width, float height, int cx, int cy) {
  float *corners = new float[6];
  corners[0] = 0;
  corners[1] = cy - height / 2;
  corners[2] = cx - width / 2;
  corners[3] = cy - height / 2;
  corners[4] = 640 - width;
  corners[5] = cy - height / 2;
  return corners;
}

int main(int argc, char **argv){
  ros::init(argc, argv, "depth_stream");
  ros::NodeHandle n;
  int width = 100;
  int height = 100;
  int cx = 320;
  int cy = 240;
  float* corners = getCorners(width, height, cx, cy);

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
      ROS_INFO("Width:%f, Height:%f\n", width, height);

      // Query the distance from the camera to the object in the center of the image
      // float dist_to_center = depth.get_distance(width / 2, height / 2);
      msg.left_depth = getAverageDepth(depth, width, height, corners[0], corners[1]);
      msg.center_depth = getAverageDepth(depth, width, height, corners[0], corners[1]);
      msg.right_depth = getAverageDepth(depth, width, height, corners[0], corners[1]);
      // Print the distance

      // Publish the message
      depth_pub.publish(msg);
      // ROS_INFO("The camera is facing an object %f meters away \n", dist_to_center);
  }
  return 0;
}
