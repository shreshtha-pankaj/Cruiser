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
        rospy.Subscriber("/camera/depth", Depth ,self.depth_callback_light)
        rospy.Subscriber("/kp", Float32 ,self.kp_callback)

        # self.straight_state =  rospy.get_param("right")
        #
        # self.kp = self.straight_state["kp"]
        # self.ki = self.straight_state["ki"]
        # self.kd = self.straight_state["kd"]

        self.lastgains = []
        self.pid = PID.PID(-1.8/1000,0,0)
        self.pid.clear()
        self.current_pose = 0
        self.current_state = 0

    def kp_callback(self,data):
        self.pid.setKp(data.data*(10**-4))
        print("kp changed to : ",data.data)

    def stateid_to_gains_reader(self):
        #Lakshya
        pass

    def current_state_callback(self,data):
        #Published by state machine 1 - straight 2 - turn right
        self.current_state = data.data
                                  
    def depth_callback_1(self,data):
        if data.left_depth > 3750:
            data.left_depth = 1800
        error = data.right_depth - data.left_depth
        if abs(error) <= 200:
            error = 0
        self.output_publisher(error)

    def depth_callback(self, data):
         #    data.right_depth = 1800
        turn_thresh = 3500
        if (data.right_depth >= turn_thresh and data.left_depth >= turn_thresh) or (data.left_depth<turn_thresh and data.right_depth <turn_thresh):
            error = data.right_depth - data.left_depth
        elif data.left_depth > turn_thresh:
            error = 2*(data.right_depth-1800)
        elif data.right_depth > turn_thresh:
            error = 2*(1800 - data.left_depth)
        if abs(error) <= 200:
            error = 0
        self.output_publisher(error)

    def depth_callback_light(self, data):
         #    data.right_depth = 1800
        error = data.di
        if abs(error) <= 15:
            error = 0
        self.output_publisher(error)


    def output_publisher(self, current_error):
        output = self.pid.update(current_error)
        output += 0.135
        if output > 0.64:
            output = 0.505
        if output < -0.64:
            outpout = -0.37
        self.output_pub.publish(output)

if __name__ == "__main__":
    rospy.init_node('pid_node')
    pid_node = pid_node()
    rospy.spin()
