#! /usr/bin/env python
import rospy
from trajectory_msgs.msg import JointTrajectoryPoint
import actionlib
import time
from std_msgs.msg import *
from state_machine.msg import *
from trajectory_msgs.msg import JointTrajectoryPoint
import time

# Default parameters to be used for the race, for other tasks, modify in the launch file
stop_motor = rospy.get_param('/master_state_machine/stop_motor', 0.0)
slow_motor = rospy.get_param('/master_state_machine/slow_motor', -0.3)
servo_zero = rospy.get_param('/master_state_machine/servo_zero', 0.135)
high_speed = rospy.get_param('/master_state_machine/high_speed', -0.6)
turn_depth = rospy.get_param('/master_state_machine/turn_depth', 8500)
reverse_motor = rospy.get_param('/master_state_machine/reverse_motor', 0.6)

print("State Machine Parameters: ", stop_motor, slow_motor, servo_zero, high_speed, turn_depth, reverse_motor)

class State():

    def __init__(self, state_name):
        self.state = ""
        pass


class Straight(State):

    def __init__(self, state_name):
        self.state_name = state_name

    def move(self, state_machine, servo=0, motor =slow_motor):
        self.state = 'straight'
        state_machine.create_trajectory_Motor_cmd_3('servo', servo)
        state_machine.create_trajectory_Motor_cmd_3('brushless_motor', motor)

class Slide(State):

    def __init__(self,state_name):
        self.state_name = state_name

    def slide(self, state_machine)
        start_time = time.time()
        #speed up
        while time.time() - start_time < 0.7:
            state_machine.create_trajectory_Motor_cmd_3('servo', servo_zero)
            state_machine.create_trajectory_Motor_cmd_3('brushless_motor', high_speed)
        
        #slide
        while time.time() - start_time < 0.9:
            state_machine.create_trajectory_Motor_cmd_3('servo', -0.5)
            state_machine.create_trajectory_Motor_cmd_3('brushless_motor', 0.6)
        while time.time() - start_time < 1.3:
            state_machine.create_trajectory_Motor_cmd_3('servo', 0.385)
            state_machine.create_trajectory_Motor_cmd_3('brushless_motor', -0.5)
        
        state_machine.create_trajectory_Motor_cmd_3('servo', servo_zero)
        state_machine.create_trajectory_Motor_cmd_3('brushless_motor', -0.3)

        #correct if neccesary

class Right(State):

    def __init__(self, state_name):
        self.state_name = state_name

    def turn(self, state_machine, servo=-0.5, motor =reverse_motor):
        turn_time = 0.017 # TODO: Should turn time be a parameter?
        end_time = time.time() + turn_time
        print("Depth while turning:left, center, right ", state_machine.left_depth,state_machine.center_depth,state_machine.right_depth)
        while time.time() < end_time:
            self.state = 'right'
            state_machine.create_trajectory_Motor_cmd_3('servo', servo)
            state_machine.create_trajectory_Motor_cmd_3('brushless_motor', motor)


class StateMachine(object):


    def __init__(self, pub_topic, sub_topic_depth, sub_topic_pid, sub_topic_stop_sign):
        self.sub_depth = rospy.Subscriber(sub_topic_depth, Depth, callback=self.sub_depth_callback)
        self.sub_pid = rospy.Subscriber(sub_topic_pid, Float32, callback=self.sub_pid_callback)
        self.sub_stop_sign = rospy.Subscriber(sub_topic_stop_sign, Bool, callback=self.sub_stop_sign_callback)
        self.center_depth, self.left_depth, self.right_depth = 0, 0, 0
        self.pololu = Polulu_Command()
        self.straight = Straight("Move-Straight")
        self.right = Right("Move-Right")
        self.slide = Slide("SLide")
        self.pid_value = 0.15
        self.is_stop_sign = False
        self.curr_turn = 1
        self.turn_flag = False
        self.turn_state_flag = False
        self.slide_time = time.time()

    def sub_depth_callback(self, data):
        self.center_depth = data.center_depth
        self.left_depth = data.left_depth
        self.right_depth = data.right_depth

    def sub_pid_callback(self, data):
        self.pid_value = data.data + servo_zero

    def create_trajectory_Motor_cmd_3(self,jnt_name, pos, speed=0):
        self.pololu.send_command(jnt_name, pos, speed)

    def sub_stop_sign_callback(self, data):
        self.is_stop_sign = data.data

    def determine_state(self):
        cur_time = time.time()
        
        # move straight when we above a certain depth threshold and not in the turning state
        if self.center_depth > turn_depth and not self.turn_state_flag:
            print('Car is moving straight(l, c, r)', self.left_depth, self.center_depth, self.right_depth)
            self.straight.move(self,servo = self.pid_value,motor=slow_motor)
        
        elif self.center_depth < turn_depth and time.time() - self.slide_time > 7:
            print('Sliding state: ', self.left_depth,self.center_depth,self.right_depth)
            self.slide_time = time.time()
            self.slide.slide(self)
            #self.turn_state_flag = False
            

        
        


class Polulu_Command:
    def __init__(self):
        self.joint_name_servo = 'servo'
        self.joint_name_brushless_motor = 'brushless_motor'
        self.pub = rospy.Publisher("/pololu/command", MotorCommand, queue_size=10)

    def send_command(self, jntName, pos, speed=0):
        mtr = MotorCommand()
        mtr.joint_name = jntName
        mtr.position = pos
        print("Sending motor: ",jntName, pos)
        mtr.speed = speed  # /self.MaxSpeed#pololu take 0 to 1.0 as speed, check the correct division
        mtr.acceleration = 1.0
        self.pub.publish(mtr)

if __name__ =='__main__':
    sub_topic_depth = '/camera/depth'
    sub_topic_pid = '/pid_output'
    sub_topic_stop_sign = '/is_stop_sign'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    time.sleep(3.5)
    ss = StateMachine(pub_topic, sub_topic_depth,sub_topic_pid,sub_topic_stop_sign)
    while not rospy.is_shutdown():
        ss.determine_state()
