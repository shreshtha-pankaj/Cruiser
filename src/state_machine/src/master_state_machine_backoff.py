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
slow_motor = rospy.get_param('/master_state_machine/slow_motor', -0.25)
servo_zero = rospy.get_param('/master_state_machine/servo_zero', 0.155)
high_speed = rospy.get_param('/master_state_machine/high_speed', -0.55)
turn_depth = rospy.get_param('/master_state_machine/turn_depth', 4500)
reverse_motor = rospy.get_param('/master_state_machine/reverse_motor', 0.4)

servo_left = 0.56
servo_right = -0.29
backoff_reverse_duration = 2
backoff_turn_duration = 1.5
backoff_straight_duration = 1


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
        state_machine.create_trajectory_Motor_cmd('servo', servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)


class Right(State):

    def __init__(self, state_name):
        self.state_name = state_name

    def turn(self, state_machine, servo=-0.5, motor =reverse_motor):
        turn_time = 0.017 # TODO: Should turn time be a parameter?
        end_time = time.time() + turn_time
        rospy.loginfo("Depth while turning:left, center, right: %f, %f, %f ", state_machine.left_depth, state_machine.center_depth,state_machine.right_depth)
        while time.time() < end_time:
            self.state = 'right'
            state_machine.create_trajectory_Motor_cmd('servo', servo)
            state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)


class Stop(State):

    def __init__(self, state_name):
        self.state_name = state_name
        self.reverse_flag= True

    def stop(self, state_machine, servo=servo_zero, motor=stop_motor):
        state_machine.create_trajectory_Motor_cmd('servo',servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)


class Reverse(State):
    def __init__(self, state_name):
        self.state_name = state_name

    def stop_and_reverse(self, state_machine, servo=servo_zero, motor=stop_motor):
        #brake
        state_machine.create_trajectory_Motor_cmd('servo',servo_zero)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)
        time.sleep(0.5)
        #zeror - reverse - zero 
        t0 = time.time()
        rospy.loginfo("Backoff: Stopping the servo")
        state_machine.create_trajectory_Motor_cmd('servo',servo_zero)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', stop_motor)
        time.sleep(0.2)
        
        # Move in reverse
        t0 = time.time()
        while(time.time() - t0 < backoff_reverse_duration and not rospy.is_shutdown() ):
            rospy.loginfo("Backoff: Giving reverse motor control: %f`", state_machine.center_depth)
            state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)

        t0 =time.time()
        while(time.time()-t0 <0.3):
            rospy.loginfo("Backoff: Stopping the servo")
            state_machine.create_trajectory_Motor_cmd('servo',servo_zero)
            state_machine.create_trajectory_Motor_cmd('brushless_motor', stop_motor)

        action_left = True
        if(state_machine.left_depth > state_machine.right_depth):
            rospy.loginfo("Backoff: Turning the servo left")
            action_left = True
            self.move_left(state_machine, servo_left)
            #turn left
        else:
            rospy.loginfo("Backoff: Turning the servo right")
            action_left = False
            self.move_right(state_machine, servo_right)
            #turn right
        rospy.loginfo("Backoff: Going straight")
        t0 = time.time()
        while(time.time() - t0 < backoff_turn_duration):
            state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)
 
        t0 = time.time()
        while(time.time() - t0 < backoff_straight_duration):
            if action_left:
                state_machine.create_trajectory_Motor_cmd('servo',servo)
            else:
                state_machine.create_trajectory_Motor_cmd('servo',servo)
            state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)
        self.reversed =True
        
        t0= time.time()
        while(time.time() - t0 < 1):
            if action_left:
               # self.move_right(state_machine, servo_right)
                state_machine.create_trajectory_Motor_cmd('servo', servo_right)
                state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)
            else:
               # self.move_left(state_machine, servo_left)
                state_machine.create_trajectory_Motor_cmd('servo', servo_left)
                state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)

    def reverse(self, state_machine, servo=servo_zero, motor=stop_motor):
        state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)

    def move_right(self, state_machine, servo_right):
        temp = 0
        while temp > servo_right:
           state_machine.create_trajectory_Motor_cmd('servo', temp)
           temp -=0.09

    def move_left(self, state_machine, servo_left):
        temp = 0
        while temp < servo_left:
            state_machine.create_trajectory_Motor_cmd('servo', temp)
            temp +=0.14


class StateMachine(object):


    def __init__(self, pub_topic, sub_topic_depth, sub_topic_pid, sub_topic_stop_sign):
        self.sub_depth = rospy.Subscriber(sub_topic_depth, Depth, callback=self.sub_depth_callback)
        self.sub_pid = rospy.Subscriber(sub_topic_pid, Float32, callback=self.sub_pid_callback)
        self.sub_stop_sign = rospy.Subscriber(sub_topic_stop_sign, Bool, callback=self.sub_stop_sign_callback)
        self.center_depth, self.left_depth, self.right_depth = 0, 0, 0
        self.pololu = Polulu_Command()
        self.straight = Straight("Move-Straight")
        self.right = Right("Move-Right")
        self.stop = Stop("Stop")
        self.reverse = Reverse("Reverse")
        self.pid_value = 0.15
        self.is_stop_sign = False
        self.curr_turn = 1
        self.turn_flag = False
        self.turn_state_flag = False

    def sub_depth_callback(self, data):
        self.center_depth = data.center_depth
        self.left_depth = data.left_depth
        self.right_depth = data.right_depth

    def sub_pid_callback(self, data):
        self.pid_value = data.data + servo_zero

    def create_trajectory_Motor_cmd(self,jnt_name, pos, speed=0):
        self.pololu.send_command(jnt_name, pos, speed)


    def sub_stop_sign_callback(self, data):
        self.is_stop_sign = data.data

    def determine_state(self):
        cur_time = time.time()
        if self.is_stop_sign:
            self.stop.stop(self)
            return

        # move straight when we above a certain depth threshold and not in the turning state
        if self.center_depth > turn_depth and not self.turn_state_flag:
            print('Car is moving straight(l, c, r) %f, %f, %f', self.left_depth, self.center_depth, self.right_depth)
            self.straight.move(self,servo = self.pid_value,motor=high_speed)

        elif self.center_depth < 1499:
            t0 = time.time()
            is_collided = True
            #########rospy.loginfo("Checking for collision: %f", self.center_depth)
            while(time.time() - t0 < 0.5):
                if(self.center_depth > 800):
                    is_collided = False
                    break
            if is_collided:
                rospy.loginfo('We collided, now we will avoid collision %f, %f, %f', self.left_depth, self.center_depth, self.right_depth)
                self.reverse.stop_and_reverse(self)
                is_collided = False    
        
        # TODO: Explain what is happening here  
        elif self.center_depth > turn_depth and self.turn_state_flag and self.center_depth > 1500:
            curr_time = time.time()
            while time.time() - curr_time < 0.5:
                self.straight.move(self,servo=0.4,motor=high_speed)
            while time.time() - curr_time < 2:
                self.straight.move(self,servo=self.pid_value,motor=high_speed)
            self.turn_state_flag = False

        # Car is turning right    
        elif self.center_depth < turn_depth and not self.turn_flag and self.center_depth >1500:
            print('Car is turning right', self.center_depth)
            self.right.turn(self)
            self.turn_flag = True
            self.turn_state_flag = True
  
        elif self.center_depth < 3000 and self.turn_flag:
            self.right.turn(self)


class Polulu_Command:
    def __init__(self):
        self.joint_name_servo = 'servo'
        self.joint_name_brushless_motor = 'brushless_motor'
        self.pub = rospy.Publisher("/pololu/command", MotorCommand, queue_size=10)

    def send_command(self, jntName, pos, speed=0):
        mtr = MotorCommand()
        mtr.joint_name = jntName
        mtr.position = pos
        mtr.speed = speed  # /self.MaxSpeed#pololu take 0 to 1.0 as speed, check the correct division
        mtr.acceleration = 1.0
        self.pub.publish(mtr)

if __name__ =='__main__':
    sub_topic_depth = '/camera/depth'
    sub_topic_pid = '/pid_output'
    sub_topic_stop_sign = '/is_stop_sign'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    time.sleep(3)
    ss = StateMachine(pub_topic, sub_topic_depth,sub_topic_pid,sub_topic_stop_sign)
    while not rospy.is_shutdown():
        ss.determine_state()
