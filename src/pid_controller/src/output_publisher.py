#!/usr/bin/python

import PID
import time
import numpy as np
import rospy
from std_msgs.msg import *
from pid_controller.msg import pid_data
#Subscibe to /pid_gains , get PID gains from State_machine - Float32[3]
#Subscribe to /current_pose , get distance from walls: - Float32[]
#Subscribe to /goal_pose, get desired pose ?? Add to /oid_gains from StateMachine?
#Publish to /pid_output, publish PID output - Float32[]


class pid_node(object):

    def __init__(self):
        
        self.output_publisher = rospy.Publisher('/pid_output',Float32, queue_size = 10)
        rospy.Subscriber("/pid_gains", pid_data,self.pid_gain_callback)
        rospy.Subscriber("/current_pose", Float32 ,self.current_pose_callback)

        self.lastgains = []
        self.pid = PID.PID()

        self.current_pose = 0

        def pid_gain_callback(self,data):
        	if lastgains == [data.kp,data.ki,data.kd]:
        		return
        	lastgains = [data.kp,data.ki,data.kd]
        	self.pid.setKp(lastgains[0])
        	self.pid.setKi(lastgains[1])
        	self.pid.setKd(lastgains[2])
        	self.pid.SetPoint = data.setPoint

        def current_pose_callback(self,data):
        	self.current_pose = data.data
        	self.output_publisher()


        def output_publisher(self):
        	self.pid.update(self.current_pose)
		output = pid.output
        	self.output_publisher.publish(output)

if __name__ == "__main__":
    rospy.init_node('pid_node')
    pid_node = pid_node()
