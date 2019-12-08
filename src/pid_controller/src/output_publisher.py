#!/usr/bin/python

import PID
import time
import numpy as np
import rospy
from std_msgs.msg import *
import sys
from pid_controller.msg import *
import yaml
#from pid_controller.msg import pid_data
#Subscibe to /pid_gains , get PID gains from State_machine - Float32[3]
#Subscribe to /current_pose , get distance from walls: - Float32[]
#Subscribe to /goal_pose, get desired pose ?? Add to /oid_gains from StateMachine?
#Publish to /pid_output, publish PID output - Float32[]

class pid_node(object):

    def __init__(self):
        
        self.output_pub = rospy.Publisher('/pid_output',Float32, queue_size = 10)
        rospy.Subscriber("/current_state", Int16 ,self.current_state_callback)
        rospy.Subscriber("/camera/depth", Depth ,self.depth_callback)
        self.lastgains = []
        self.pid = PID.PID(0.25/2000,0,0.25/2000000)
        self.pid.clear()
        self.current_pose = 0
        self.current_state = 0
        self.error_thresh = 125

    def stateid_to_gains_reader(self):
        pass

    def current_state_callback(self,data):
        #Published by state machine 1 - straight 2 - turn right
        self.current_state = data.data

    def depth_callback(self,data):
	    # if data.left_depth > 3700:
	    #     data.left_depth = 1800
        #     error = data.right_depth - data.left_depth

        # Use right depth if we find left depth spurious
        if data.left_depth > 2200:
            error = data.right_depth - 1750
            print('Spurious left depth (l, r, error)', data.left_depth, data.right_depth, error)

        # Use left depth if we find right depth spurious    
        elif data.right_depth > 2200:
            error = 1750 - data.left_depth
            print('Spurious right depth (l, r, error)', data.left_depth, data.right_depth, error)

        # Use both if they are within bounds
        else:
            error = data.right_depth - data.left_depth
            print('Within bounds (l, r, error)', data.left_depth, data.right_depth, error)

	    if abs(error) <= self.error_thresh:
            error = 0
	    self.output_publisher(error)


    def output_publisher(self, current_error):
        output = self.pid.update(current_error)
        self.output_pub.publish(output)

if __name__ == "__main__":
    rospy.init_node('pid_node')
    pid_node = pid_node()
    rospy.spin()
