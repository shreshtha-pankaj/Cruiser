#!/usr/bin/python

import numpy as np
import rospy
from std_msgs.msg import *
import sys
from pid_controller.msg import *
#from pid_controller.msg import pid_data
#Subscibe to /pid_gains , get PID gains from State_machine - Float32[3]
#Subscribe to /current_pose , get distance from walls: - Float32[]
#Subscribe to /goal_pose, get desired pose ?? Add to /oid_gains from StateMachine?
#Publish to /pid_output, publish PID output - Float32[]

if __name__ == "__main__":
    rospy.init_node('kp__node')
    output_pub = rospy.Publisher('/kp',Float32, queue_size = 1)
    while not rospy.is_shutdown():
        kp = input("Enter KP: ")
        output_pub.publish(kp)
