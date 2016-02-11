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
servo_zero = rospy.get_param('/master_state_machine/servo_zero', 0.08)
high_speed = rospy.get_param('/master_state_machine/high_speed', -0.70)
turn_depth = rospy.get_param('/master_state_machine/turn_depth', 6000)
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
        #state_machine.create_trajectory_Motor_cmd_2([servo,motor])
        state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_servo, servo)
        state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_brushless_motor, motor)


class Right(State):

    def __init__(self, state_name):
        self.state_name = state_name

    def turn(self, state_machine, servo=-0.6, motor =-0.25):
        turn_time = 0.05 # TODO: Should turn time be a parameter?
        end_time = time.time() + turn_time
        print("Depth while turning:left, center, right ", state_machine.left_depth,state_machine.center_depth,state_machine.right_depth)
        while time.time() < end_time:
            self.state = 'right'
            state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_servo, servo)
            state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_brushless_motor, motor)
            #state_machine.create_trajectory_Motor_cmd_2([servo,motor])

class Left(State):

    def __init__(self, state_name):
        self.state_name = state_name

    def turn(self, state_machine, servo=0.73, motor =-0.25):
        turn_time = 0.05 # TODO: Should turn time be a parameter?
        end_time = time.time() + turn_time
        print("Depth while turning:left, center, right ", state_machine.left_depth,state_machine.center_depth,state_machine.right_depth)
        while time.time() < end_time:
            self.state = 'right'
            state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_servo, servo)
            state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_brushless_motor, motor)
            #state_machine.create_trajectory_Motor_cmd_2([servo,motor])


class Stop(State):

    def __init__(self, state_name):
        self.state_name = state_name
        self.reverse_flag= True

    def stop(self, state_machine, servo=servo_zero, motor=reverse_motor):
        #state_machine.create_trajectory_Motor_cmd_2([servo,motor])
        state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_servo, servo)
        state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_brushless_motor, motor)
        if self.reverse_flag:
            state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_brushless_motor, reverse_motor)
            # state_machine.create_trajectory_Motor_cmd('brushless_motor', reverse_motor)
            self.reverse_flag= False
            time.sleep(0.5)
        state_machine.create_trajectory_Motor_cmd_3(state_machine.pololu.joint_name_brushless_motor, motor)
        # state_machine.create_trajectory_Motor_cmd('brushless_motor', motor)


class StateMachine(object):


    def __init__(self, pub_topic, sub_topic_depth, sub_topic_pid, sub_topic_pid_light, sub_topic_stop_sign):
        self.sub_depth = rospy.Subscriber(sub_topic_depth, Depth, callback=self.sub_depth_callback)
        self.sub_pid = rospy.Subscriber(sub_topic_pid, Float32, callback=self.sub_pid_callback)
        self.sub_pid_light = rospy.Subscriber(sub_topic_pid, Float32, callback=self.sub_pid_light_callback)
        self.sub_stop_sign = rospy.Subscriber(sub_topic_stop_sign, Bool, callback=self.sub_stop_sign_callback)
        self.pololu = Polulu_Command()
        self.center_depth, self.left_depth, self.right_depth = 0, 0, 0
        self.straight = Straight("Move-Straight")
        self.right = Right("Move-Right")
        self.left = Left("Move-Left")
        self.stop = Stop("Stop")
        self.pid_value, self.pid_light_value = 0, 0
        self.is_stop_sign = False
        self.curr_turn = 1
        self.turn_state_flag = False
        self.start_flag = True
        self.is_in_turn = False
        self.turn_timestamp = time.time() + 0
        self.time_wait = 0
        self.slow_down_depth = turn_depth + 2500
        self.light_flag = False
        rospy.loginfo("slow_down_depth %f", self.slow_down_depth)
        self.turn_count = 0
        self.no_of_turns = 0
        self.start_time = time.time()

    def sub_depth_callback(self, data):
        self.center_depth = data.center_depth
        self.left_depth = data.left_depth
        self.right_depth = data.right_depth

    def sub_pid_callback(self, data):
        self.pid_value = data.data
        if self.pid_value >0.2:
            self.pid_value = 0.2
        elif self.pid_value <-0.12:
            self.pid_value = -0.12


    def sub_pid_light_callback(self, data):
        self.pid_light_value = data.data

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


    def create_trajectory_Motor_cmd_3(self,jnt_name, pos, speed=0):
        self.pololu.send_command(jnt_name, pos, speed)

    def sub_stop_sign_callback(self, data):
        self.is_stop_sign = data.data

    def determine_state(self):
        if time.time()-self.start_time > 16.5:
            self.straight.move(self, servo=self.pid_value, motor = high_speed)

        global turn_depth
        if self.start_flag:
            tim = time.time()
            while(time.time() - tim < 3):
                self.straight.move(self, servo=servo_zero, motor = high_speed)
            self.start_flag = False
        cur_time = time.time()
        if self.is_stop_sign:
            self.stop.stop(self)
            return


        # if self.center_depth < turn_d move straight when we above a certain depth threshold and not in the turning state
        if (self.center_depth > turn_depth or time.time() - self.turn_timestamp < self.time_wait) and not self.turn_state_flag:
            rospy.loginfo('Car is moving straight(l, c, r): %f, %f, %f, %f', self.left_depth, self.center_depth, self.right_depth, self.pid_value)
            if self.center_depth < self.slow_down_depth  and time.time() - self.turn_timestamp > self.time_wait:
                rospy.loginfo("slowing down------->>>>>>>")
                self.straight.move(self,servo = self.pid_value, motor=0.75)
            else:
                if self.light_flag:
                    print('Using light flag:')
                    self.straight.move(self,servo = self.pid_light_value, motor = high_speed)
                else:
                    self.straight.move(self,servo = self.pid_value, motor = high_speed)
            self.turn_count  =  0


        # TODO: Explain what is happening here
        elif self.center_depth > turn_depth and self.turn_state_flag:
            curr_time = time.time()
            turn_depth = 5500
            print('Correcting after turn state with center depth: ',self.center_depth)
            self.turn_timestamp = curr_time
            if self.turn_count >4:
                self.no_of_turns +=1
                print("Turn completed :",self.no_of_turns)
                if self.no_of_turns ==1:
                    turn_depth= 4500
                    self.slow_down_depth = 8000
                #self.time_wait = 4.8
                    self.light_flag = False
                else:
                    self.light_flag = False


                
            while time.time() - curr_time < 0.3:
                self.straight.move(self,servo=-0.33,motor=-0.5)
            self.turn_state_flag = False
            self.turn_count=0

        # Too close to an obstacle, STOP
        elif self.center_depth < 1200:
            #stop the car for now.
            #print('Car is stopping', self.center_depth)
            self.stop.stop(self)

        # Car is turning right
        elif self.center_depth < turn_depth:
            self.left.turn(self)
            turn_depth = 5700
            self.turn_state_flag = True
            self.turn_count +=1


       #elif self.center_depth < 5500:# and self.right_depth > 3000:# and self.turn_flag:
            #self.right.turn(self)



class Polulu_Command:
    def __init__(self):
        self.joint_name_servo = 'servo'
        self.joint_name_brushless_motor = 'brushless_motor'
        self.pub=rospy.Publisher("/pololu/command",MotorCommand,queue_size=10)
    
    def send_command(self, jntName, pos, speed=0):
        mtr=MotorCommand()
        mtr.joint_name=jntName
        mtr.position=pos
        mtr.speed=speed#/self.MaxSpeed#pololu take 0 to 1.0 as speed, check the correct division
        mtr.acceleration=1.0
        self.pub.publish(mtr)


if __name__ =='__main__':
    sub_topic_depth = '/camera/depth'
    sub_topic_pid = '/pid_output'
    sub_topic_pid_light = '/pid_output_light'
    sub_topic_stop_sign = '/is_stop_sign'
    pub_topic = '/car_state'
    rospy.init_node('car_state_pub')
    time.sleep(3.5)
    ss = StateMachine(pub_topic, sub_topic_depth, sub_topic_pid, sub_topic_pid_light, sub_topic_stop_sign)
    ss.pololu.send_command('servo',0)
    rospy.loginfo('Initializing Master State Machine')
    while not rospy.is_shutdown():
        # if True:#not ss.is_in_turn:
        ss.determine_state()
