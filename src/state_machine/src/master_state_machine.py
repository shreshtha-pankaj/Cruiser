#! /usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectoryPoint
import actionlib

from std_msgs.msg import *
from state_machine.msg import *
from trajectory_msgs.msg import JointTrajectoryPoint

names=['servo','brushless_motor']

class state_machine(object):
    def __init__(self, pub_topic, sub_topic_depth, sub_topic_pid):
        self.client = actionlib.SimpleActionClient('pololu_trajectory_action_server', pololu_trajectoryAction)

        self.ptopic = pub_topic
        self.sub_topic_depth = sub_topic_depth
        self.sub_depth = rospy.Subscriber(self.sub_topic_depth, Depth, callback=self.sub_depth_callback)
        self.sub_pid = rospy.Subscriber(self.sub_topic_pid, Float, callback=self.sub_callback)
        self.cnt_wall_distance = 0
        self.straight = Straight("Move-Straight")
        self.right = Right("Move-Right")

    def sub_depth_callback(self, data):
        #  get the all the depths
	    self.cnt_wall_distance = data.center_depth
        self.left_wall_distance = data.left_depth
        self.right_wall_distance = data.right_depth

    def sub_pid_callback(self, data):
    #  get the pid value
    self.pid_value = -1*data.data

    def create_trajectory_Motor_cmd(self, jntName, pos, speed=0):
        goal = pololu_trajectoryGoal()
        traj = goal.joint_trajectory
        traj.header.stamp = rospy.Time.now()
        traj.joint_names.append(jntName)
        pts = JointTrajectoryPoint()
        pts.time_from_start = rospy.Duration(0.0)
        pts.positions.append(float(pos))
        pts.velocities.append(speed)
        traj.points.append(pts)
        self.client.send_goal(goal)
        self.client.wait_for_result(rospy.Duration.from_sec(3.0))

    def determine_state(self):
        depth_data = self.cnt_wall_distance


        if depth_data > 5000:
            self.straight.move(servo = self.pid_value)
        elif depth_data <= 5000 and depth_data > 1000:
            self.right.move(self, servo = self.pid_value)
        else:
            #stop the car for now.
            self.straight.move(self,servo = 0.15, motor = 0)       

class Straight(State):
    def __init__(self, state_name):
        self.state_name = state_name
    
    def move(self, state_machine, servo=0, motor =-1.0):
        state_machine.create_trajectory_Motor_cmd('servo', servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)

class Right(State):
    def __init__(self, state_name):
        self.state_name = state_name
    
    def move(self, state_machine, servo=0, motor =-1.0):
        state_machine.create_trajectory_Motor_cmd('servo', servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)


class State():
    def __init__(self, state_name):

if __name__ =='__main__':

    # publishing to ros_pololu_servo right now

    # publish pos and vel data
    sub_topic_depth = '/depth_frames'
    sub_topic_pid = '/pid_otput'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    ss = state_machine(pub_topic= pub_topic, sub_topic_depth=sub_topic_depth, sub_topic_pid = sub_topic_pid)
    ss.client.wait_for_server()
    while not rospy.is_shutdown():
	   ss.determine_state()