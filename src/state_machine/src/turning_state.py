#! /usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectoryPoint
import actionlib
import time
from std_msgs.msg import *
from state_machine.msg import *
from trajectory_msgs.msg import JointTrajectoryPoint

names=['servo','brushless_motor']



class turning_state_machine(object):
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

	def turn_state(self):
		straight_time = 1
		end_time = time.time() + straight_time

		while time.time() < end_time:
			self.create_trajectory_Motor_cmd('servo', 0)
			self.create_trajectory_Motor_cmd('brushless_motor', -1.0)

		turn_time = 1.5

		end_time = time.time() + turn_time

		while time.time() < end_time:
			self.create_trajectory_Motor_cmd('servo', 0.5)
			self.create_trajectory_Motor_cmd('brushless_motor', -0.5)
		
		self.create_trajectory_Motor_cmd('servo', 0)
        self.create_trajectory_Motor_cmd('brushless_motor', 0)



if __name__ =='__main__':

	# publishing to ros_pololu_servo right now

	# publish pos and vel data
	pub_topic = '/car_state'
	rospy.init_node('turn_state_pub')
	ss = turning_state_machine(pub_topic= pub_topic)
	ss.client.wait_for_server()
	ss.turn_state()