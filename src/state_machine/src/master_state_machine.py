#! /usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectoryPoint
import actionlib

from std_msgs.msg import *
from state_machine.msg import *
from trajectory_msgs.msg import JointTrajectoryPoint

names=['servo','brushless_motor']

class state_machine(object):
    def __init__(self, pub_topic, sub_topic):
        self.client = actionlib.SimpleActionClient('pololu_trajectory_action_server', pololu_trajectoryAction)

        self.ptopic = pub_topic
        self.stopic = sub_topic
        self.sub = rospy.Subscriber(self.stopic, Depth, callback=self.sub_callback)

        self.cnt_wall_distance = 0

    def sub_callback(self, data):
        #  get the z value
	self.cnt_wall_distance = data.center_depth


    def create_trajectory_Motor_cmd(self, jntName, pos, speed=0):
        # mtr = MotorCommand()
        # mtr.joint_name = jntName
        # mtr.position = pos
        # mtr.speed = speed  # /self.MaxSpeed#pololu take 0 to 1.0 as speed, check the correct division
        # mtr.acceleration = 1.0
        # self.pub.publish(mtr)
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


#MOTOR RANGES: -0.2 (walks) to -0.35


    def determine_state(self):
        depth_data = self.cnt_wall_distance
        if depth_data > 5000:
            self.create_trajectory_Motor_cmd('servo', 0)
            self.create_trajectory_Motor_cmd('brushless_motor', -0.35)

        elif depth_data <= 5000 and depth_data > 2000:
            self.create_trajectory_Motor_cmd('servo', 0.5)
            self.create_trajectory_Motor_cmd('brushless_motor', -0.2)
        else:
	    
            self.create_trajectory_Motor_cmd('servo', 0)
            self.create_trajectory_Motor_cmd('brushless_motor', 0)


if __name__ =='__main__':

    # publishing to ros_pololu_servo right now

    # publish pos and vel data
    sub_topic = '/depth_frames'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    ss = state_machine(pub_topic= pub_topic, sub_topic=sub_topic)
    ss.client.wait_for_server()
    while not rospy.is_shutdown():
	   ss.determine_state()
