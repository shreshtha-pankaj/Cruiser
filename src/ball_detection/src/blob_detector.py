#!/usr/bin/env python
import rospy
import cv2
import numpy as np;
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
 

class BlobDetector:
    def __init__(self):
        rgb_topic = '/camera/rgb'
        depth_topic = '/camera/depth'
        # Set up the detector with default parameters.
        self.detector = cv2.SimpleBlobDetector()
        self.pub = rospy.Publisher('ball_detected', Bool, queue_size=50)
        self.sub = rospy.Subscriber(rgb_topic, Image, self.rgb_callback)
        self.bridge = CvBridge()
        self.is_ball = False
    
    def rgb_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data,"mono8")
            # cv_image = cv2.resize(cv_image,(253,200))
            # Detect blobs.
            keypoints = detector.detect(im)
            rospy.loginfo('Keypoints in image, ', keypoints)
            # Draw detected blobs as red circles.
            # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
            im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)         
            # Show keypoints
            cv2.imshow("Keypoints", im_with_keypoints)
            cv2.waitKey(0)

            if len(keypoints) > 0:
                if self.is_ball == False:
                    self.is_ball = True
                    self.pub.publish(self.is_ball)
            else:
                if self.is_ball:
                    self.is_ball = False
                    self.pub.publish(self.is_ball)
        except CvBridgeError as e:
            rospy.logerr(str(e))
        
if __name__ == '__main__':
    rospy.init_node('blob_detector', log_level = rospy.INFO, anonymous=True)
    listener = BlobDetector()
    rospy.spin()