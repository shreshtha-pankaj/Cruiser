#! /usr/bin/env python

import rospy
import actionlib

from ros_pololu_servo.msg import *
from trajectory_msgs.msg import JointTrajectoryPoint

names=['servo','brushless_motor']


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

if __name__ == '__main__':
    rospy.init_node('pololu_car_pub')
    pololu = Polulu_Command()
    while not rospy.is_shutdown():
        print "Enter servo Position: "
        servo_pos = float(raw_input())
        print ("Got servo input %f", servo_pos)
        print ("Enter motor Position: ")
        motor_pos = float(raw_input())
        print ("Got motor input %f", motor_pos)

        pololu.send_command(pololu.joint_name_servo,servo_pos)
        pololu.send_command(pololu.joint_name_brushless_motor,motor_pos)

    # Shutdown
    pololu.send_command(self.joint_name_servo, 0.135)
    pololu.send_command(self.joint_name_brushless_motor, 0.0)
    print "Reset and Shutdown successful!"

