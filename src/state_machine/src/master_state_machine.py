#! /usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectoryPoint
import actionlib
import time
from std_msgs.msg import *
from state_machine.msg import *
from trajectory_msgs.msg import JointTrajectoryPoint

names=['servo','brushless_motor']


stop_motor = rospy.get_param('/master_state_machine/stop_motor', 0.0)
slow_motor = rospy.get_param('/master_state_machine/slow_motor', -0.43)
servo_zero = rospy.get_param('/master_state_machine/servo_zero', 0.155)
print("State Machine Parameters: ", stop_motor, slow_motor, servo_zero)
class State():
    def __init__(self, state_name):
        pass

class Straight(State):
    def __init__(self, state_name):
        self.state_name = state_name

    def move(self, state_machine, servo=0, motor =slow_motor):
        state_machine.create_trajectory_Motor_cmd('servo', servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)

class Right(State):
    def __init__(self, state_name):
        self.state_name = state_name

    def turn(self, state_machine, servo=-0.5, motor =slow_motor):
        turn_time = 0.15
        end_time = time.time() + turn_time

        while time.time() < end_time:
            state_machine.create_trajectory_Motor_cmd('servo', servo)
            state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)

class Stop(State):
    def __init__(self, state_name):
        self.state_name = state_name

    def stop(self, state_machine, servo=0, motor=stop_motor):
        state_machine.create_trajectory_Motor_cmd('servo',servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor',motor)

class state_machine(object):
    def __init__(self, pub_topic, sub_topic_depth, sub_topic_pid):
        self.client = actionlib.SimpleActionClient('pololu_trajectory_action_server', pololu_trajectoryAction)
        self.sub_depth = rospy.Subscriber(sub_topic_depth, Depth, callback=self.sub_depth_callback)
        self.sub_pid = rospy.Subscriber(sub_topic_pid, Float32, callback=self.sub_pid_callback)
        self.sub_stop_sign = rospy.Subscriber(sub_topic_stop_sign, Bool, callback=self.sub_stop_sign_callback)
        self.cnt_wall_distance = 0
        self.straight = Straight("Move-Straight")
        self.right = Right("Move-Right")
        self.stop = Stop("Stop")
        self.pid_value = 0.15
        self.is_stop_sign = False

    def sub_depth_callback(self, data):
        #  get the all the depths
        self.cnt_wall_distance = data.center_depth
        self.left_wall_distance = data.left_depth
        self.right_wall_distance = data.right_depth

    def sub_pid_callback(self, data):
        #  get the pid value
        self.pid_value = data.data + servo_zero
        # print("Current PID Value :",self.pid_value)

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

    def sub_stop_sign_callback(self, data):
        self.is_stop_sign = data.data

    def determine_state(self):
        depth_data = self.cnt_wall_distance
        if self.is_stop_sign:
            self.stop.stop(self)

        if depth_data >3000:
            self.straight.move(self,servo = self.pid_value)
        elif depth_data <=3000 and depth_data > 1500:
            print("depth", depth_data)
            self.right.turn(self)
        else:
            #stop the car for now.
            self.stop.stop(self)

if __name__ =='__main__':

    # publishing to ros_pololu_servo right now
    import time
    time.sleep(5)
    # publish pos and vel data
    sub_topic_depth = '/camera/depth'
    sub_topic_pid = '/pid_output'
    sub_topic_stop_sign = '/is_stop_sign'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    ss = state_machine(pub_topic, sub_topic_depth,sub_topic_pid)
    ss.client.wait_for_server()
    while not rospy.is_shutdown():
        ss.determine_state()
