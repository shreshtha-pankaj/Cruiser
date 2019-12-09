#!/usr/bin/env python
import rospy
import cv2
from std_msgs.msg import Bool
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class StopSignDetector:
    def __init__(self, topic):
        self.topic = topic
        self.pub = rospy.Publisher('is_stop_sign', Bool, queue_size=30)
        self.sub = rospy.Subscriber(topic, Image, self.stopSignDetectorCallback)
        self.bridge = CvBridge()
        self.classifier_file = "/home/odroid/Cruiser/src/stop_sign/src/stopsign_classifier.xml"
        self.classifier = cv2.CascadeClassifier(self.classifier_file)
        self.is_stop_sign = False
        self.frame_count = 0

    def stopSignDetectorCallback(self, data):
        if self.frame_count % 8 != 0:
            self.frame_count += 1
            return
        self.frame_count = 1
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data,"mono8")
            cv_image = cv2.resize(cv_image,(253,200))
        except CvBridgeError as e:
            rospy.logerr(e)
        stop_signs = self.classifier.detectMultiScale(cv_image,1.02,10)

        # Detected Stop Sign
        if len(stop_signs) > 0:
            if self.is_stop_sign == False:
                self.is_stop_sign = True
                self.pub.publish(self.is_stop_sign)
        else:
            if self.is_stop_sign:
                self.is_stop_sign = False
                self.pub.publish(self.is_stop_sign)


def main():
    topic = '/camera/image'
    listener = StopSignDetector(topic)
    rospy.spin()

if __name__ == '__main__':
    node_name = 'stop_sign'
    rospy.init_node(node_name, log_level = rospy.INFO, anonymous=True)
    main()
