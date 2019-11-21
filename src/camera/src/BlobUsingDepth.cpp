#include <opencv2/opencv.hpp>
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <camera/Depth.h>
#include <librealsense2/rs.hpp>
#include <list>
using namespace cv;

std::vector<cv::KeyPoint> findBlobs(cv::Mat color);

std::vector<cv::KeyPoint> findBlobs(cv::Mat color){
	// Read image
	
	// Set up the detector with default parameters.
	cv::SimpleBlobDetector detector;
	
	// Detect blobs.
	std::vector<cv::KeyPoint> keypoints;
	detector.detect( color, keypoints);
	
	// Draw detected blobs as red circles.
	// DrawMatchesFlags::DRAW_RICH_KEYPOINTS flag ensures the size of the circle corresponds to the size of blob
	cv::Mat im_with_keypoints;
	cv::drawKeypoints( color, keypoints, im_with_keypoints, cv::Scalar(0,0,255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS );
	
	// Show blobs
	cv::imshow("keypoints", im_with_keypoints );
	cv::waitKey(0);

}

int main(int argc, char **argv){
  ros::init(argc, argv, "depth_stream");
  ros::NodeHandle n;
  int width_dim = 100;
  int height_dim = 50;
  int depth_width = 640;
  int depth_height = 480;
  // int cx = depth_width / 2;
  // int cy = depth_height / 2;
  // float* corners = getCorners(width_dim, height_dim, cx, cy);
  // Create a publisher node
  ros::Publisher depth_pub = n.advertise<camera::Depth>("depth_frames_blob", 1000);

  // Instantiate an instance of a message
  camera::Depth msg;
  // Create a Pipeline - this serves as a top-level API for streaming and processing frames
  rs2::pipeline p;
  // Configure and start the pipeline
  rs2::config config;
  config.enable_stream(RS2_STREAM_DEPTH, depth_width, depth_height, RS2_FORMAT_Z16, 30);
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
	  cv::Mat color(cv::Size(640,480), CV_8UC3, (void*)frames.get_data(), cv::Mat::AUTO_STEP);

      std::vector<cv::KeyPoint> blobs = findBlobs(color);
          ROS_INFO("Done....");
      // Query the distance from the camera to the object in the center of the image
	//     float dist_to_center = depth.get_distance(depth_width, depth_height);
    //   msg.left_depth = getAverageDepth(depth, width_dim, height_dim, corners[0], corners[1]);
    //   msg.center_depth = getAverageDepth(depth, width_dim, height_dim, corners[2], corners[3]);
    //   msg.right_depth = getAverageDepth(depth, width_dim, height_dim, corners[4], corners[5]);
      // Publish the message
      //depth_pub.publish("Hello blob");

  }
  return 0;
}