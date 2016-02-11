#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <librealsense2/rs.hpp>
#include <opencv2/opencv.hpp> //? to include in Cmake

// https://github.com/IntelRealSense/librealsense/blob/master/doc/stepbystep/getting_started_with_openCV.md
int main(int argc, char **argv){
  ros::init(argc, argv, "color_stream");
  ros::NodeHandle n;
  // Create a publisher node
 // ros::Publisher depth_pub = n.advertise<camera::Depth>("color_frames", 1000);

  // Create a Pipeline - this serves as a top-level API for streaming and processing frames
  rs2::pipeline pipe;

  // Configure and start the pipeline
  rs2::config config;
  config.enable_stream(RS2_STREAM_COLOR, 640, 480, RS2_FORMAT_BGR8, 30);

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
      rs2::frame color = frames.get_color_frame();

      // Creating OpenCV Matrix from a color image
      Mat color(Size(640, 480), CV_8UC3, (void*)color_frame.get_data(), Mat::AUTO_STEP);
      ROS_INFO("%d", color.get_data_size());
      // Display in a GUI
      namedWindow("Display Image", WINDOW_AUTOSIZE );
      imshow("Display Image", color);
  }
  return 0;
}
