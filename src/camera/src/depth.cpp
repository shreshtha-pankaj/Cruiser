#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <algorithm>
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

float getAverageDepthLR(rs2::depth_frame& depth, float width, float height, int x, int y) {
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

int getMedian(rs2::depth_frame& depth, float width, float height) {
  float sum = 0;
  int ctr = 0;
  int size = width;
  int start = height/2 - 5;
  int end = height/2 + 5;
  float arr[size];
  int len = end -start + 1;
  float temp[len];
  int c = 0;
  for(int i = 0; i < width; i++) {
    for (int j = start, k =0; j < end ; j++,k++) {
      float depth_val = depth.get_distance(i,j);
      temp[k] = depth_val;
    }
    std::sort(temp, temp + (len -1));
    arr[i] = temp[len/2];

  }
  float max = 0;
  for(int i=0; i< size;i++){
    if(arr[i]>max){
      max = arr[i];
    }
  }
  return max;
}

float getAverageDepthMedian(rs2::depth_frame& depth, float width, float height, int x, int y) {
  float sum = 0;
  int ctr = 0;
  int size = height*width;
  int median = size/2;
  float arr[size];
  int c = 0;
  for(int i = y; i < y + height; i++) {
    for (int j = x; j < x + width; j++) {
      float depth_val = depth.get_distance(j,i);
      arr[c] = depth_val;
      c++;
    }
  }
  std::sort(arr, arr + size);
  return arr[median]*1000;
}

float* getCorners(float width, float height, int cx, int cy) {
  float *corners = new float[6];
  // TODO: need to check what the right value is, with 1280 * 960, we used 20, avoiding noisy edges
  corners[0] = 20;
  corners[1] = (cy - height / 2);
  corners[2] = (cx - width / 2);
  corners[3] = (cy - height / 2);
  // TODO: need to check what the right value is, with 1280 * 960, we used 20
  corners[4] = (depth_width - width - 20);
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

  int width_dim = 40;
  int height_dim = 50;
  int width_dim_LR = 50;
  int height_dim_LR = 50;
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

       msg.left_depth = getAverageDepthLR(depth, width_dim_LR, height_dim_LR, corners[0], corners[1]);
       msg.center_depth = getAverageDepth(depth, width_dim, height_dim, corners[2], corners[3]);
       msg.right_depth = getAverageDepthLR(depth, width_dim_LR, height_dim_LR, corners[4], corners[5]);

//      msg.left_depth = getAverageDepthMedian(depth, width_dim_LR, height_dim_LR, corners[0], corners[1]);
   //   msg.center_depth = getAverageDepthMedian(depth, width_dim, height_dim, corners[2], corners[3]);
     // msg.right_depth = getAverageDepthMedian(depth, width_dim_LR, height_dim_LR, corners[4], corners[5]);
      msg.di = getMedian(depth, depth_width, depth_height);
      depth_pub.publish(msg);

  }
  return 0;
}
