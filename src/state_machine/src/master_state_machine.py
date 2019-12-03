#! /usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectoryPoint
import actionlib
import time
from std_msgs.msg import *
from state_machine.msg import *
from trajectory_msgs.msg import JointTrajectoryPoint
from sensor_msgs.msg import Imu as imu_msg

names=['servo','brushless_motor']

stop_motor = 0.0
slow_motor =  -0.25
servo_zero = 0.155
high_speed = -0.45
reverse_motor = 0.3
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
        turn_time = 0.017
        end_time = time.time() + turn_time

        while time.time() < end_time:
            state_machine.create_trajectory_Motor_cmd('servo', servo)
            state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)

class Stop(State):
    def __init__(self, state_name):
        self.state_name = state_name
        self.reverse_flag= True

    def stop(self, state_machine, servo=servo_zero, motor=stop_motor):
        state_machine.create_trajectory_Motor_cmd('servo',servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', stop_motor)
        #time.sleep(0.5)
        if(self.reverse_flag):
            state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)
            self.reverse_flag= False
            time.sleep(0.5)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', stop_motor)

class state_machine(object):
    def __init__(self, pub_topic, sub_topic_depth, sub_topic_pid, sub_topic_stop_sign, imu_tpoic):
        self.client = actionlib.SimpleActionClient('pololu_trajectory_action_server', pololu_trajectoryAction)
        self.sub_depth = rospy.Subscriber(sub_topic_depth, Depth, callback=self.sub_depth_callback)
        self.sub_pid = rospy.Subscriber(sub_topic_pid, Float32, callback=self.sub_pid_callback)
        self.sub_stop_sign = rospy.Subscriber(sub_topic_stop_sign, Bool, callback=self.sub_stop_sign_callback)
        self.sub_imu = rospy.Subscriber(imu_tpoic, imu_msg, callback=self.sub_imu_callback)
        self.cnt_wall_distance = 0
        self.straight = Straight("Move-Straight")
        self.right = Right("Move-Right")
        self.stop = Stop("Stop")
        self.pid_value = 0.15
        self.is_stop_sign = False
        self.curr_turn = 1

    def sub_depth_callback(self, data):
        #  get the all the depths
        self.cnt_wall_distance = data.center_depth
        self.left_wall_distance = data.left_depth
        self.right_wall_distance = data.right_depth

    def sub_pid_callback(self, data):
        #  get the pid value
        self.pid_value = data.data + servo_zero
        #print("Current PID Value :",self.pid_value)
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

    def sub_imu_callback(self, data):
        print(data)

#MOTOR RANGES: -0.2 (walks) to -0.35


    def determine_state(self):
        depth_data = self.cnt_wall_distance
        if self.is_stop_sign:
            start_time = time.time()
            while(time.time() - start_time < 2.2):
                self.stop.stop(self)
            return

        if depth_data > 8000:
            print('Straight fast', depth_data)
            self.straight.move(self,servo = self.pid_value,motor=high_speed)
        elif depth_data < 1200:
            #stop the car for now.
            print('Stop', depth_data)
            self.stop.stop(self)
        else:
            # if self.curr_turn == 1:
            self.depth_for_turn(depth_data, 4700)
            #     self.curr_turn = 2
            # else:
            #     self.depth_for_turn(depth_data, 3500)

    def depth_for_turn(self, depth_data, depth_val):
        if depth_data > depth_val and depth_data <= 8000:
            print('Straight Slow', depth_data)
            self.straight.move(self,servo=self.pid_value)
        elif depth_data <= depth_val and depth_data > 1200:
            print('turn right', depth_data)
            # print("depth", depth_data)
            self.right.turn(self)

if __name__ =='__main__':

    # publishing to ros_pololu_servo right now
    import time
    time.sleep(5)
    # publish pos and vel data
    sub_topic_depth = '/depth_frames'
    sub_topic_pid = '/pid_output'
    sub_topic_stop_sign = '/is_stop_sign'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    imu_tpoic = 'imu/data_raw'
    ss = state_machine(pub_topic, sub_topic_depth,sub_topic_pid,sub_topic_stop_sign, imu_tpoic)
    ss.client.wait_for_server()
    while not rospy.is_shutdown():
        ss.determine_state()
