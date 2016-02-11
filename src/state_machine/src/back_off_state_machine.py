#! /usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectoryPoint
import actionlib
import time
from std_msgs.msg import *
from state_machine.msg import *
from trajectory_msgs.msg import JointTrajectoryPoint
from sensor_msgs.msg import Imu as imu_msg
import time

names=['servo','brushless_motor']

stop_motor = 0.0
slow_motor =  -0.22
servo_zero = 0.155
servo_left = 0.55
servo_right = -0.25
high_speed = -0.22
reverse_motor = 0.4
backoff_reverse_duration = 2
backoff_turn_duration = 1.5
backoff_straight_duration = 1


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

    def turn(self, state_machine, servo=-0.20, motor =slow_motor):
        turn_time = 0.012
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

class Reverse(State):
    def __init__(self, state_name):
        self.state_name = state_name

    def stop_and_reverse(self, state_machine, servo=servo_zero, motor=stop_motor):
        state_machine.create_trajectory_Motor_cmd('servo',servo_zero)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', stop_motor)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', stop_motor)
        time.sleep(1)

        # Move in reverse
        t0 = time.time()
        while(time.time() - t0 < backoff_reverse_duration and  not rospy.is_shutdown() ):
            print("Giving reverse motor control: ", state_machine.cnt_wall_distance)
            state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)
    
        print("Stopping the servo")
        state_machine.create_trajectory_Motor_cmd('servo',servo_zero)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', stop_motor)
        time.sleep(0.5)
        #self.left_wall_distance, self.cnt_wall_distance, self.right_wall_distance
        what_i_did = 1
        if(state_machine.left_wall_distance - state_machine.right_wall_distance > 1000):
            print("Turning the servo left")
            what_i_did = 1
            state_machine.create_trajectory_Motor_cmd('servo',servo_left)
            #turn left
        else:
            print("Turning the servo right")
            what_i_did = 0
            state_machine.create_trajectory_Motor_cmd('servo',servo_right)
            #turn right
        print("Going straight")
        t0 = time.time()
        while(time.time() - t0 < backoff_turn_duration):
            state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)
 
        t0 = time.time()
        while(time.time() - t0 < backoff_straight_duration):
            state_machine.create_trajectory_Motor_cmd('servo',servo)
            state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)
        self.reversed =True
        
        t0= time.time()
	while( time.time() - t0<1):
            if what_i_did:
                state_machine.create_trajectory_Motor_cmd('servo',servo_right)
                state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)
            else:
                state_machine.create_trajectory_Motor_cmd('servo',servo_left)
                state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)

    def reverse(self, state_machine, servo=servo_zero, motor=stop_motor):
        state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)

class state_machine(object):
    def __init__(self, pub_topic, sub_topic_depth, sub_topic_pid, sub_topic_stop_sign, imu_topic):
        self.client = actionlib.SimpleActionClient('pololu_trajectory_action_server', pololu_trajectoryAction)
        self.sub_depth = rospy.Subscriber(sub_topic_depth, Depth, callback=self.sub_depth_callback)
        self.sub_pid = rospy.Subscriber(sub_topic_pid, Float32, callback=self.sub_pid_callback)
        self.sub_stop_sign = rospy.Subscriber(sub_topic_stop_sign, Bool, callback=self.sub_stop_sign_callback)

#        self.sub_imu = rospy.Subscriber(imu_topic, imu_msg, callback=self.sub_imu_callback)
        self.cnt_wall_distance = 0
        self.straight = Straight("Move-Straight")
        self.right = Right("Move-Right")
        self.stop = Stop("Stop")
        self.reverse = Reverse("Reverse")
        self.pid_value = 0.15
        self.is_stop_sign = False
        self.curr_turn = 1

    def sub_depth_callback(self, data):
        #  get the all the depths
        self.cnt_wall_distance = data.center_depth
        self.left_wall_distance = data.left_depth
        self.right_wall_distance = data.right_depth

    def sub_pid_callback(self, data):
        self.pid_value = data.data + servo_zero

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

    # def sub_imu_callback(self, data):
    #     print('Angular velocity: ', data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z)
    #     print('Linear Acceleration', data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z)

    def determine_state(self):
        if self.is_stop_sign:
            start_time = time.time()
            while(time.time() - start_time < 2.2):
                self.stop.stop(self)
            return
        
        if self.cnt_wall_distance > 3500:
            print('Straight fast', self.cnt_wall_distance)
            self.straight.move(self,servo = self.pid_value,motor=high_speed)

        elif self.cnt_wall_distance < 800:
            #stop the car for now.
            t0 = time.time()
            is_collided = True
            print("Checking for collision:", self.cnt_wall_distance)
            while(time.time() - t0 < 0.5):
                if(self.cnt_wall_distance > 500):
                    is_collided = False
                    break
            if is_collided:
                print('We collided, now avoid collision', self.left_wall_distance, self.cnt_wall_distance, self.right_wall_distance)
                self.reverse.stop_and_reverse(self)
                is_collided = False
        else:
            self.right.turn(self)
            print("turn right", self.cnt_wall_distance)

if __name__ =='__main__'
    sub_topic_depth = '/camera/depth'
    sub_topic_pid = '/pid_output'
    sub_topic_stop_sign = '/is_stop_sign'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    imu_topic = 'imu/data_raw'
    ss = state_machine(pub_topic, sub_topic_depth,sub_topic_pid,sub_topic_stop_sign, imu_topic)
    ss.client.wait_for_server()
    while not rospy.is_shutdown():
        ss.determine_state()


