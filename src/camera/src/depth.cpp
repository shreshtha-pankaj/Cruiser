#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <camera/Depth.h>
#include <librealsense2/rs.hpp>

int depth_width, depth_height, frame_rate;

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
  // TODO: need to check what the right value is, with 1280 * 960, we used 20, avoiding noisy edges
  corners[0] = 10;
  corners[1] = (cy - height / 2);
  corners[2] = (cx - width / 2);
  corners[3] = (cy - height / 2);
  // TODO: need to check what the right value is, with 1280 * 960, we used 20
  corners[4] = (depth_width - width - 10);
  corners[5] = (cy - height / 2);
  return corners;
}

int main(int argc, char **argv){
  ros::init(argc, argv, "depth_stream");
  ros::NodeHandle n;
  
  // Default Parameters (to be used for race)
  n.param("/depth_stream/frame_rate", frame_rate, 60);
  n.param("/depth_stream/resolution_height", depth_height, 480);
  n.param("/depth_stream/resolution_width", depth_width, 640);
  
  ROS_INFO("Depth Parameters: %d, %d, %d", frame_rate, depth_height, depth_width);

  int width_dim = 50;
  int height_dim = 50;
  int cx = depth_width / 2;
  int cy = depth_height / 2;
  float* corners = getCorners(width_dim, height_dim, cx, cy);

  ros::Publisher depth_pub = n.advertise<camera::Depth>("camera/depth", 1000);
  camera::Depth msg;
  rs2::pipeline pipe;
  rs2::config config;
  config.enable_stream(RS2_STREAM_DEPTH, depth_width, depth_height, RS2_FORMAT_Z16, frame_rate);
  pipe.start(config);

  // Camera warmup - dropping several first frames to let auto-exposure stabilize
  rs2::frameset frames;
  for(int i = 0; i < 30; i++)
  {
      //Wait for all configured streams to produce a frame
      frames = pipe.wait_for_frames();
  }

  while (ros::ok())
  {
      frames = pipe.wait_for_frames();
      rs2::depth_frame depth = frames.get_depth_frame();

      msg.left_depth = getAverageDepth(depth, width_dim, height_dim, corners[0], corners[1]);
      msg.center_depth = getAverageDepth(depth, width_dim, height_dim, corners[2], corners[3]);
      msg.right_depth = getAverageDepth(depth, width_dim, height_dim, corners[4], corners[5]);

      depth_pub.publish(msg);

  }
  return 0;
}
