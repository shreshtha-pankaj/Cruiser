#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image as msg_Image
from cv_bridge import CvBridge, CvBridgeError


class ImageListener:
    def __init__(self, topic):
        self.height_dim, self.width_dim = 8, 16
        self.corners = self.get_corners(self.height_dim, self.width_dim, 240, 320)
        self.topic = topic
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber(topic, msg_Image, self.imageDepthCallback)

    def imageDepthCallback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, data.encoding)
            pix = (data.width/2, data.height/2)
            print(data.width, data.height)
            left_depth = self.getAverageDepth(cv_image, self.width_dim, self.height_dim, self.corners[0], self.corners[1])
            cen_depth = self.getAverageDepth(cv_image, self.width_dim, self.height_dim, self.corners[2], self.corners[3])
            right_depth = self.getAverageDepth(cv_image, self.width_dim, self.height_dim, self.corners[4], self.corners[5])
            print("Left Depth: ", left_depth)
            print("Center Depth: ", center_depth)
            print("Right Depth: ", right_depth)
            # cen_depth = cv_image[pix[1], pix[0]]
            # if depth_at_cen
            # print('%s: Depth at center(%d, %d): %f(mm)\r' % (self.topic, pix[0], pix[1], cv_image[pix[1], pix[0]]))
        except CvBridgeError as e:
            print(e)
            return

    def get_corners(self, height, width, cy, cx):
        corners = []
        # left_frame
        corners += [ 0, cy - height / 2 ]
        # center_frame
        corners += [cx - width / 2, cy - height / 2]
        # right_frame
        corners += [ 640 - width, cy - height / 2] # 640 is the image width
        print(corners)
        return corners



    def getAverageDepth(self, img, width_dim, height_dim, x, y):
        sum = 0
        ctr = 0
        for i in range(y, y + height_dim):
            for j in range(x, x + width_dim):
                if img[y, x]:
                    ctr += 1
                    sum = sum + img[y, x]
        return (sum / ctr);


def main():
    topic = '/camera/depth/image_rect_raw'
    listener = ImageListener(topic)
    rospy.spin()

if __name__ == '__main__':
    node_name = 'depth_listener'
    rospy.init_node(node_name)
    main()
