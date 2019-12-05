#include "ros/ros.h"
#include "std_msgs/String.h"
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sstream>
#include <librealsense2/rs.hpp>
#include <opencv2/opencv.hpp> //? to include in Cmake
// https://github.com/IntelRealSense/librealsense/blob/master/doc/stepbystep/getting_started_with_openCV.md
int main(int argc, char **argv){
  ros::init(argc, argv, "color_stream");
  ros::NodeHandle n;
  int height, width, frame_rate;
  n.param("/color_stream/frame_rate", frame_rate, 30);
  n.param("/color_stream/resolution_height",height, 480);
  n.param("/color_stream/resolution_width", width, 640);
  ROS_INFO("Color parameters: %d, %d, %d", frame_rate, height, width);

  image_transport::ImageTransport it(n);
  image_transport::Publisher pub = it.advertise("camera/image", 1);

  // Create a Pipeline - this serves as a top-level API for streaming and processing frames
  rs2::pipeline pipe;

  // Configure and start the pipeline
  rs2::config config;
  config.enable_stream(RS2_STREAM_COLOR, width, height, RS2_FORMAT_BGR8, frame_rate);

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
      // Block program until frames arrive
      frames = pipe.wait_for_frames();

      // Try to get a frame of a depth image
      rs2::frame color_frames = frames.get_color_frame();

      // Creating OpenCV Matrix from a color image

     // cv::Size size(256,192);
     // cv::Mat color_dest;
      cv::Mat color(cv::Size(640,480), CV_8UC3, (void*)color_frames.get_data(), cv::Mat::AUTO_STEP);
     // cv::resize(color, color_dest, size);
      sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", color).toImageMsg();
      pub.publish(msg);
      // ROS_INFO("%d", color.get_data_size());
  }
  return 0;
}
