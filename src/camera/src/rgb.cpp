// https://github.com/IntelRealSense/librealsense/blob/master/doc/stepbystep/getting_started_with_openCV.md

#include "ros/ros.h"
#include "std_msgs/String.h"
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sstream>
#include <librealsense2/rs.hpp>
#include <opencv2/opencv.hpp> 

int main(int argc, char **argv){
  ros::init(argc, argv, "color_stream");
  ros::NodeHandle n;
  int height, width, frame_rate;

  // Default parameters to be used for STOP SIGN
  n.param("/color_stream/frame_rate", frame_rate, 30);
  n.param("/color_stream/resolution_height",height, 480);
  n.param("/color_stream/resolution_width", width, 640);
  ROS_INFO("Color parameters: %d, %d, %d", frame_rate, height, width);

  image_transport::ImageTransport it(n);
  image_transport::Publisher pub = it.advertise("camera/image", 1000);

  rs2::pipeline pipe;
  rs2::config config;
  config.enable_stream(RS2_STREAM_COLOR, width, height, RS2_FORMAT_BGR8, frame_rate);
  pipe.start(config);

  // Camera warmup - dropping several first frames to let auto-exposure stabilize
  rs2::frameset frames;
  for(int i = 0; i < 30; i++)
  {
      frames = pipe.wait_for_frames();
  }

  while (ros::ok())
  {
      frames = pipe.wait_for_frames();
      rs2::frame color_frames = frames.get_color_frame();
      cv::Mat color(cv::Size(width, height), CV_8UC3, (void*)color_frames.get_data(), cv::Mat::AUTO_STEP);
      sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", color).toImageMsg();
      pub.publish(msg);
  }
  return 0;
}
