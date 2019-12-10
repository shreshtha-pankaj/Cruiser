#!/usr/bin/env python
import rospy
import cv2
import numpy as np;
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Bool

cyanLower = (80, 110, 120)
cyanUpper = (180, 255, 255)

class BlobDetector:
    def __init__(self):
        rgb_topic = '/camera/image'

        # Set up the detector with default parameters.
        self.detector = cv2.SimpleBlobDetector()
        self.pub = rospy.Publisher('ball_detected', Bool, queue_size=50)
        self.sub = rospy.Subscriber(rgb_topic, Image, self.rgb_callback)
        self.bridge = CvBridge()
        self.is_ball = False
        self.frame_count = 0
    
    def rgb_callback(self, data):
        if self.frame_count %4 !=0:
            self.frame_count +=1
            return
        self.frame_count = 1
        try:
            start_time = time.time()
            #  check if it should be bgr8 or rgb8
            frame = self.bridge.imgmsg_to_cv2(data,"bgr8")
            frame = cv2.resize(frame,(320,240))
#            frame = imutils.resize(frame, width=200)
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv, cyanLower, cyanUpper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            center = None
            # only proceed if at least one contour was found
            if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                # only detect ball if the radius meets a minimum size
                if radius > 10:
                    cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 1)
                    #cv2.circle(frame, center, 5, (0, 0, 255), -1)
                    # publish only while transitioning from ball detected to not
                    if self.is_ball == False:
                        self.is_ball = True
                        self.pub.publish(self.is_ball)
                        rospy.loginfo("Ball Detection: We see a ball rolling towards us")
                else:
                    if self.is_ball:
                        self.is_ball = False
                        self.pub.publish(self.is_ball)
                        rospy.loginfo("Ball Detection: We don't see a ball anymore")

            # Removed tracking code as we don't need it
          
            # show the frame to our screen
    #        cv2.imshow("Frame", frame)
    #        key = cv2.waitKey(1) & 0xFF
        except CvBridgeError as e:
            rospy.logerr(str(e))
            
        
if __name__ == '__main__':
    rospy.init_node('ball_detection', log_level = rospy.INFO, anonymous=True)
    listener = BlobDetector()
    rospy.spin()
