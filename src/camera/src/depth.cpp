#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <camera/Depth.h>
#include <librealsense2/rs.hpp>

int depth_width = 640;
int depth_height = 480;

float getAverageDepth(rs2::depth_frame& depth, float width, float height, int x, int y) {
  float sum = 0;
  int ctr = 0;
  for(int i = y; i < y + height; i++) {
    for (int j = x; j < x + width; j++) {
      float depth_val = depth.get_distance(j,i);
      if (depth_val > 0) {
        ctr += 1;
        sum += depth_val;
      }
    }
  }
  if (ctr == 0) {
    return 0;
  }
  return (1000*sum / ctr);
}

float* getCorners(float width, float height, int cx, int cy) {
  float *corners = new float[6];
  corners[0] = 0; // need to check what the right value is, with 1280 * 960, we used 20
  corners[1] = (cy - height / 2);
  corners[2] = (cx - width / 2);
  corners[3] = (cy - height / 2);
  corners[4] = (depth_width - width);
  corners[5] = (cy - height / 2);
  return corners;
}

int main(int argc, char **argv){
  ros::init(argc, argv, "depth_stream");
  ros::NodeHandle n;
  int width_dim = 50;
  int height_dim = 50;
  int cx = depth_width / 2;
  int cy = depth_height / 2;
  float* corners = getCorners(width_dim, height_dim, cx, cy);
  // Create a publisher node
  ros::Publisher depth_pub = n.advertise<camera::Depth>("depth_frames", 1000);

  // Instantiate an instance of a message
  camera::Depth msg;
  // Create a Pipeline - this serves as a top-level API for streaming and processing frames
  rs2::pipeline p;
  // Configure and start the pipeline
  rs2::config config;
  config.enable_stream(RS2_STREAM_DEPTH, depth_width, depth_height, RS2_FORMAT_Z16, 60);
  p.start(config);
  while (ros::ok())
  {
      // Block program until frames arrive
      rs2::frameset frames = p.wait_for_frames();

      // Try to get a frame of a depth image
      rs2::depth_frame depth = frames.get_depth_frame();

      // Get the depth frame's dimensions
      float width = depth.get_width();
      float height = depth.get_height();
      // Query the distance from the camera to the object in the center of the image
      msg.left_depth = getAverageDepth(depth, width_dim, height_dim, corners[0], corners[1]);
      msg.center_depth = getAverageDepth(depth, width_dim, height_dim, corners[2], corners[3]);
      msg.right_depth = getAverageDepth(depth, width_dim, height_dim, corners[4], corners[5]);
      // Publish the message
      depth_pub.publish(msg);

  }
  return 0;
}
