#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <camera/Depth.h>
#include <librealsense2/rs.hpp>
#include <list> 
#include "Blob.cpp"


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
  int cx = depth_width / 2;
  int cy = depth_height / 2;
  float* corners = getCorners(width_dim, height_dim, cx, cy);
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
      depth_pub.publish("Hello blob");

  }
  return 0;
}


list<ns::Blob> findBlobs(rs2::depth_frame depthFrame, float width, float height){
    float trackedDepth = 2500;
    float threshold = 25;
    
    // Begin loop to walk through every pixel
  for (int x = 0; x < width; x++ ) {
        for (int y = 0; y < height; y++ ) {
            int loc = x + y * width;
            float depth_val = depth.get_distance(y,x);
                    
            float d = distSqDepth(depth_val, tracked_depth); 

            if (d < threshold*threshold) {
                bool found = false;
                for (ns::Blob b : blobs) {
                    if (b.isNear(x, y)) {
                        b.add(x, y);
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    ns::Blob b = new ns::Blob(x, y);
                    blobs.add(b);
                }
            }
        }
    }
}


float distSq(float x1, float y1, float x2, float y2) {
  float d = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
  return d;
}

float distSqDepth(float d1, float d2) {
  return (d2-d1)*(d2-d1);  
}

