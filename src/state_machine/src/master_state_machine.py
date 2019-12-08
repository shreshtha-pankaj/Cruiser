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
turn_depth = rospy.get_param('/master_state_machine/turn_depth', 5500)
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
        state_machine.create_trajectory_Motor_cmd_2([servo,motor])

class Right(State):

    def __init__(self, state_name):
        self.state_name = state_name

    def turn(self, state_machine, servo=-0.5, motor =reverse_motor):
        turn_time = 0.017 # TODO: Should turn time be a parameter?
        end_time = time.time() + turn_time
        print("Depth while turning:left, center, right ", state_machine.left_depth,state_machine.center_depth,state_machine.right_depth)
        while time.time() < end_time:
            self.state = 'right'
            state_machine.create_trajectory_Motor_cmd_2([servo,motor])

class Stop(State):

    def __init__(self, state_name):
        self.state_name = state_name
        self.reverse_flag= True

    def stop(self, state_machine, servo=servo_zero, motor=reverse_motor):
        state_machine.create_trajectory_Motor_cmd_2([servo,motor])
        if self.reverse_flag:
            state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)
            self.reverse_flag= False
            time.sleep(0.5)
        state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)


class StateMachine(object):


    def __init__(self, pub_topic, sub_topic_depth, sub_topic_pid, sub_topic_stop_sign):
        self.client = actionlib.SimpleActionClient('pololu_trajectory_action_server', pololu_trajectoryAction)
        self.sub_depth = rospy.Subscriber(sub_topic_depth, Depth, callback=self.sub_depth_callback)
        self.sub_pid = rospy.Subscriber(sub_topic_pid, Float32, callback=self.sub_pid_callback)
        self.sub_stop_sign = rospy.Subscriber(sub_topic_stop_sign, Bool, callback=self.sub_stop_sign_callback)
        self.center_depth, self.left_depth, self.right_depth = 0, 0, 0
        self.straight = Straight("Move-Straight")
        self.right = Right("Move-Right")
        self.stop = Stop("Stop")
        self.pid_value = 0.15
        self.is_stop_sign = False
        self.curr_turn = 1
        self.turn_flag = False
        self.turn_state_flag = False
        self.r_c = 0
        self.l_c = 0
        self.l_r = 0

    def sub_depth_callback(self, data):       
        self.center_depth = data.center_depth
        self.left_depth = data.left_depth
        self.right_depth = data.right_depth
   
    def sub_pid_callback(self, data):
        self.pid_value = data.data + servo_zero

    def create_trajectory_Motor_cmd(self, jntName, pos, speed=0):
        T0 = time.time()
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

    def create_trajectory_Motor_cmd_2(self, pos, speed=0):
        T0 = time.time()
        goal = pololu_trajectoryGoal()
        traj = goal.joint_trajectory
        traj.header.stamp = rospy.Time.now()
        traj.joint_names.append('servo')
        traj.joint_names.append('brushless_motor')
        pts = JointTrajectoryPoint()
        pts.time_from_start = rospy.Duration(0.0)
        pts.positions.append(float(pos[0]))
        pts.positions.append(float(pos[1]))
        pts.velocities.append(speed)
        pts.velocities.append(speed)
        traj.points.append(pts)
        self.client.send_goal(goal)
        self.client.wait_for_result(rospy.Duration.from_sec(3.0))

    def sub_stop_sign_callback(self, data):
        self.is_stop_sign = data.data

    def determine_state(self):
        # TODO: Removed local variable depth_data, don't think we need it, Check this
        # TODO: depth_data = self.center_depth
        cur_time = time.time()

        if self.is_stop_sign:
            self.stop.stop(self)
            return

        # move straight when we above a certain depth threshold and not in the turning state
        if self.center_depth > turn_depth and not self.turn_state_flag:
            print('Car is moving straight(l, c, r)', self.left_depth, self.center_depth, self.right_depth)
            self.straight.move(self,servo = self.pid_value,motor=high_speed)
#            self.turn_flag = False
     
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

        # Car is turning right (center - right) is to avoid the doorways on the track
        if not self.turn_flag and self.center_depth < turn_depth:
            print('Car is turning right', self.left_depth, self.center_depth, self.right_depth)
            self.right.turn(self)
            self.turn_flag = True
            self.turn_state_flag = True

        # TODO: Explain what is happening here    
        elif self.center_depth < 3000 and self.turn_flag:
            self.right.turn(self)


if __name__ =='__main__':
    # TODO: time.sleep(5) : Check if we need these as we drop rgb and depth frames. 
    time.sleep(3.5)
    sub_topic_depth = '/camera/depth'
    sub_topic_pid = '/pid_output'
    sub_topic_stop_sign = '/is_stop_sign'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    ss = StateMachine(pub_topic, sub_topic_depth,sub_topic_pid,sub_topic_stop_sign)
    ss.client.wait_for_server()
    while not rospy.is_shutdown():
        ss.determine_state()
