#!/usr/bin/env python
import rospy
import cv2
from std_msgs.msg import Bool

class StopSignDetector:
    def __init__(self, topic):

        
        self.topic = topic
        self.rate = rospy.Rate(10) # 10hz
        self.pub = rospy.Publisher('stop_sign_pub', Bool, queue_size=100)
        self.sub = rospy.Subscriber(topic, msg_img, self.stopSignDetectorCallback)
        self.msg = False




    def stopSignDetectorCallback(self, data):
        
        classifier_file = "stopsign_classifier.xml"
        classifier = cv2.CascadeClassifier(classifier_file)
        # img = cv2.imread("img1.jpg")
        stop_signs = classifier.detectMultiScale(data.img,1.02,10)
        if stop_signs:
            self.msg = True
            # print(stop_signs)
        else:
            self.msg = False
        self.pub.publish(self.msg)
        self.rate.sleep()
    
    

def main():
    topic = '/camera/color_frames'
    listener = StopSignDetector(topic)
    rospy.spin()

if __name__ == '__main__':
    node_name = 'stop_sign_detector'
    rospy.init_node(node_name, anonymous=True)
    main()


