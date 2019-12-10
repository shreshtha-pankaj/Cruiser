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
slow_motor = rospy.get_param('/master_state_machine/slow_motor', -0.22)
servo_zero = rospy.get_param('/master_state_machine/servo_zero', 0.155)
high_speed = rospy.get_param('/master_state_machine/high_speed', -0.22)
turn_depth = rospy.get_param('/master_state_machine/turn_depth', 4500)
reverse_motor = rospy.get_param('/master_state_machine/reverse_motor', 0.6)

servo_left = 0.4
servo_right = -0.25
backoff_reverse_duration = 2
backoff_turn_duration = 0.5
backoff_straight_duration = 0.5

print("State Machine Parameters: ", stop_motor, slow_motor, servo_zero, high_speed, turn_depth, reverse_motor)

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

    def turn(self, state_machine, servo=-0.5, motor =reverse_motor):
        turn_time = 0.017 # TODO: Should turn time be a parameter?
        end_time = time.time() + turn_time
        print("Depth while turning:left, center, right ", state_machine.left_depth,state_machine.center_depth,state_machine.right_depth)
        while time.time() < end_time:
            state_machine.create_trajectory_Motor_cmd('servo', servo)
            state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)


class AvoidBall():

    def __init__(self):
        pass

    def avoid_ball(self, state_machine, servo=0.5, motor=stop_motor):

        state_machine.create_trajectory_Motor_cmd('servo',servo_left)
        t0 = time.time()
        while(time.time() - t0 < backoff_turn_duration):
            state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)
 
        t0 = time.time()
        state_machine.create_trajectory_Motor_cmd('servo',servo_zero)
        while(time.time() - t0 < backoff_straight_duration):
            state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)

        t0= time.time()
        state_machine.create_trajectory_Motor_cmd('servo',servo_right)
	while( time.time() - t0<0.5):
            state_machine.create_trajectory_Motor_cmd('brushless_motor', slow_motor)

class Stop(State):

    def __init__(self, state_name):
        self.state_name = state_name
        self.reverse_flag= True

    def stop(self, state_machine, servo=servo_zero, motor=stop_motor):
        state_machine.create_trajectory_Motor_cmd('servo',servo)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)
        if self.reverse_flag:
            state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)
            self.reverse_flag= False
            time.sleep(0.5)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)


class StateMachine(object):


    def __init__(self, pub_topic, sub_topic_depth, sub_topic_pid, sub_topic_ball):
        self.client = actionlib.SimpleActionClient('pololu_trajectory_action_server', pololu_trajectoryAction)
        self.sub_depth = rospy.Subscriber(sub_topic_depth, Depth, callback=self.sub_depth_callback)
        self.sub_pid = rospy.Subscriber(sub_topic_pid, Float32, callback=self.sub_pid_callback)
        self.sub_ball = rospy.Subscriber(sub_topic_ball, Bool, callback = self.sub_ball_callback)
        # self.sub_stop_sign = rospy.Subscriber(sub_topic_stop_sign, Bool, callback=self.sub_stop_sign_callback)
        self.center_depth, self.left_depth, self.right_depth = 0, 0, 0
        self.straight = Straight("Move-Straight")
        self.right = Right("Move-Right")
        self.stop = Stop("Stop")
        self.avoid = AvoidBall()
        self.pid_value = 0.15
        self.is_stop_sign = False
        self.curr_turn = 1
        self.turn_flag = False
        self.turn_state_flag = False
        self.is_ball = False

    def sub_depth_callback(self, data):
        self.center_depth = data.center_depth
        self.left_depth = data.left_depth
        self.right_depth = data.right_depth

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

    def sub_ball_callback(self, data):
        self.is_ball = data.data

    def determine_state(self):
        if self.is_ball:
            self.avoid.avoid_ball(self)
            return

        # move straight when we above a certain depth threshold and not in the turning state
        if self.center_depth > turn_depth and not self.turn_state_flag:
            print('Car is moving straight(l, c, r)', self.left_depth, self.center_depth, self.right_depth)
            self.straight.move(self,servo = self.pid_value,motor=high_speed)
        
        # TODO: Explain what is happening here  
        elif self.center_depth > turn_depth and self.turn_state_flag:
            curr_time = time.time()
            while time.time() - curr_time < 0.5:
                self.straight.move(self,servo=0.4,motor=high_speed)
            while time.time() - curr_time < 2:
                self.straight.move(self,servo=self.pid_value,motor=high_speed)
            self.turn_state_flag = False

        # Too close to an obstacle, STOP    
        elif self.center_depth < 1200:
            #stop the car for now.
            print('Car is stopping', self.center_depth)
            self.stop.stop(self)

        # Car is turning right    
        elif self.center_depth < turn_depth and not self.turn_flag:
            print('Car is turning right', self.center_depth)
            self.right.turn(self)
            self.turn_flag = True
            self.turn_state_flag = True
  
        elif self.center_depth < 3000 and self.turn_flag:
            self.right.turn(self)



if __name__ =='__main__':
    sub_topic_depth = '/camera/depth'
    sub_topic_pid = '/pid_output'
    sub_topic_ball = '/ball_detected'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    ss = StateMachine(pub_topic, sub_topic_depth, sub_topic_pid, sub_topic_ball)
    ss.client.wait_for_server()
    while not rospy.is_shutdown():
        ss.determine_state()
