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
high_speed = -0.55

reverse_motor = 0.3
class State():
    def __init__(self, state_name):
        self.state = ""
        pass

class Straight(State):
    def __init__(self, state_name):
        self.state_name = state_name

    def move(self, state_machine, servo=0, motor =slow_motor):
        self.state = 'straight'
        state_machine.create_trajectory_Motor_cmd('servo', servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)

class Right(State):
    def __init__(self, state_name):
        self.state_name = state_name

    def turn(self, state_machine, servo=-0.5, motor =stop_motor):
        #turn_time = 0.017
        #end_time = time.time() + turn_time
        #state_machine.prev_cnt_depth = state_machine.cnt_wall_distance
        print("Depth while turning:left,center,right ", state_machine.left_wall_distance,state_machine.cnt_wall_distance,state_machine.right_wall_distance)

        #while time.time() < end_time:
        self.state = 'right'
        state_machine.create_trajectory_Motor_cmd('servo', servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)

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
        self.cnt_wall_distance = 0
        self.turn_flag = False
        self.turn_state_flag = False
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
        print('-----------------------------------------------------------------------------------------------')
        print('Angular velocity: ', data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z)
        print('Linear Acceleration', data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z)
        print('-----------------------------------------------------------------------------------------------')
#MOTOR RANGES: -0.2 (walks) to -0.35


    def determine_state(self):
        cur_time = time.time()
        self.prev_cnt_depth = self.cnt_wall_distance
#        print("Prev, current depth",self.prev_cnt_depth,self.cnt_wall_distance)
#        print("Turn Flag: ",self.turn_flag)
        #if abs(self.prev_cnt_depth - self.cnt_wall_distance)>3000:
        #    self.turn_flag_time = time.time()
        #    self.turn_flag = False
        #    print("Flag turned False")            
        #if cur_time - self.turn_flag_time > 1.5:
        #    self.turn_flag = True
        depth_data = self.cnt_wall_distance
        if self.is_stop_sign:
            #start_time = time.time()
            #while(time.time() - start_time < 2.2):
            self.stop.stop(self)
            return

        if depth_data > 6000 and not self.turn_state_flag:
            print('Straight fast:left, center, right',self.left_wall_distance, depth_data, self.right_wall_distance)
            self.straight.move(self,servo = self.pid_value,motor=high_speed)
        elif depth_data > 6000 and self.turn_state_flag:
            curr_time = time.time()
            while time.time() - curr_time < 2:
                self.straight.move(self,servo=self.pid_value,motor=high_speed)
            self.turn_state_flag = False
        elif depth_data < 1200:
            #stop the car for now.
            print('Stop', depth_data)
            self.stop.stop(self)
        elif depth_data < 6000 and not self.turn_flag:
            # if self.curr_turn == 1:
            #if self.turn_flag:
            print("calling turn right --------------------------")
            self.depth_for_turn(depth_data, 4700)
            self.turn_flag = True
            self.turn_state_flag = True
        elif depth_data < 3000 and self.turn_flag:
            self.right.turn(self)
            #     self.curr_turn = 2
            # else:
            #     self.depth_for_turn(depth_data, 3500)

    def depth_for_turn(self, depth_data, depth_val):
        #if depth_data > depth_val and depth_data <= 8000:
        #    print('Straight Slow', depth_data)
        #    self.straight.move(self,servo=self.pid_value)
        #elif depth_data <= depth_val and depth_data > 1200:
        #print('turn right', depth_data)
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
