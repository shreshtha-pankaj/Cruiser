#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image as msg_Image
from camera.msg import *
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as panda

class ImageListener:
    def __init__(self, topic):
        self.height_dim, self.width_dim = 50, 100
        self.corners = self.get_corners(self.height_dim, self.width_dim, 240, 320)
        self.topic = topic
        self.bridge = CvBridge()
        self.rate = rospy.Rate(10) # 10hz
        self.pub = rospy.Publisher('depth_frames', Depth, queue_size=100)
        self.sub = rospy.Subscriber(topic, msg_Image, self.imageDepthCallback)
        self.msg = Depth()

    def imageDepthCallback(self, data):
        try:
           # print(type(data))
            cv_image = self.bridge.imgmsg_to_cv2(data, data.encoding)
           # from pprint import pprint
           # panda.savetxt("foo-bar.csv" , cv_image, delimiter=",")
	   # print(cv_image[20:25, 0:20])
            pix = (data.width/2, data.height/2)
            self.msg.left_depth = self.getAverageDepth(cv_image, self.width_dim, self.height_dim, self.corners[0], self.corners[1])
            self.msg.center_depth = self.getAverageDepth(cv_image, self.width_dim, self.height_dim, self.corners[2], self.corners[3])
            self.msg.right_depth = self.getAverageDepth(cv_image, self.width_dim, self.height_dim, self.corners[4], self.corners[5])
            self.pub.publish(self.msg)
            self.rate.sleep()
        except CvBridgeError as e:
            print(e)
            return

    def get_corners(self, height, width, cy, cx):
        corners = []
        # left_frame
        corners += [ 40, cy - height / 2 ]
        # center_frame
        corners += [cx - width / 2, cy - height / 2]
        # right_frame
        corners += [ 600 - width, cy - height / 2] # 640 is the image width
        return corners



    def getAverageDepth(self, img, width_dim, height_dim, x, y):
        sum_ = 0
        ctr = 0
        #print("getAverageDepth, " ,x,"    ----   ", y," Shape : ",img.shape)
        for i in range(y, y + height_dim):
            for j in range(x, x + width_dim):
                if img[y, x] > 0:
                    ctr += 1
                    sum_ += img[y, x]
        if ctr == 0:
            
	    print("Ctr was zero ----- :(")
            return 0
        return (sum_ / ctr);


def main():
    topic = '/camera/depth/image_rect_raw'
    listener = ImageListener(topic)
    rospy.spin()

if __name__ == '__main__':
    node_name = 'depth_listener'
    rospy.init_node(node_name, anonymous=True)
    main()
