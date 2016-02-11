#! /usr/bin/env python

import rospy
import actionlib

from ros_pololu_servo.msg import *
from trajectory_msgs.msg import JointTrajectoryPoint

names=['servo','brushless_motor']

if __name__ == '__main__':
    rospy.init_node('pololu_car_pub')
    client = actionlib.SimpleActionClient('pololu_trajectory_action_server', pololu_trajectoryAction)
    print('Here')
    client.wait_for_server()
    print("connected to server")
    print("hello")
    while not rospy.is_shutdown():
        print "Enter servo Position: "
        servo_pos = raw_input()
        print ("Got servo input %f", servo_pos)
        print ("Enter motor Position: ")
        motor_pos = raw_input()
        print ("Got motor input %f", motor_pos)

        goal = pololu_trajectoryGoal()
        traj = goal.joint_trajectory
        traj.header.stamp = rospy.Time.now()
        traj.joint_names.append(names[0])
        traj.joint_names.append(names[1])
        pts=JointTrajectoryPoint()
        pts.time_from_start=rospy.Duration(0.0)
        pts.positions.append(float(servo_pos))
        pts.positions.append(float(motor_pos))
        pts.velocities.append(1.0)
        pts.velocities.append(1.0)
        traj.points.append(pts)
        client.send_goal(goal)
        client.wait_for_result(rospy.Duration.from_sec(3.0))



    # Shutdown
    pts = JointTrajectoryPoint()
    pts.time_from_start = rospy.Duration(0.0)
    pts.positions.append(0.0)
    pts.positions.append(0.0)
    pts.velocities.append(0.0)
    pts.velocities.append(0.0)
    traj.points.append(pts)
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration.from_sec(5.0))
    print "Reset and Shutdown successful!"
