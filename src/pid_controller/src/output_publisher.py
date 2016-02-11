#!/usr/bin/python
servo_zero = 0.05
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
        rospy.Subscriber("/kp", Float32 ,self.kp_callback)

        self.lastgains = []
        self.pid = PID.PID(0.18/2000,0,0)
        self.pid.clear()
        self.current_pose = 0
        self.current_state = 0


        # Changes for light
        rospy.Subscriber("/camera/depth", Depth, self.depth_callback_light)
        self.output_pub_light = rospy.Publisher('/pid_output_light',Float32, queue_size = 10)
        self.pid_light = PID.PID(-3.6 / 1000, 0, 0)
        self.pid_light.clear()

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
        if data.left_depth == 0:
            data.left_depth = 1800
        turn_thresh = 3300
        if (data.right_depth >= turn_thresh and data.left_depth >= turn_thresh) or (data.left_depth<turn_thresh and data.right_depth <turn_thresh):
            error = data.right_depth - data.left_depth
        elif data.left_depth > turn_thresh:
            print('Using right depth: ',data.left_depth,data.center_depth,data.right_depth)
            error = 2*(data.right_depth-1800)
        elif data.right_depth > turn_thresh:
            print('Using left depth: ',data.left_depth,data.center_depth,data.right_depth)
            error = 2*(1800 - data.left_depth)
        else:
            print('Else condition in error')
            error = data.right_depth - data.left_depth
        if abs(error) <= 200:
            error = 0
        self.output_publisher(error)


    def output_publisher(self, current_error):
        output = self.pid.update(current_error)
        output += servo_zero
        if output > 0.75:
            output = 0.75
        if output < -0.75:
            output = -0.75
        self.output_pub.publish(output)

    def depth_callback_light(self, data):
        error = data.di
        # if abs(error) <= 15:
        #     error = 0
        self.output_publisher_light(error)

    def output_publisher_light(self, current_error):
        output = self.pid_light.update(current_error)
        output += servo_zero
        if output > 0.7:
            output = 0.7
        if output < -0.7:
            output = -0.7
        self.output_pub_light.publish(output)

if __name__ == "__main__":
    rospy.init_node('pid_node')
    pid_node = pid_node()
    rospy.spin()
