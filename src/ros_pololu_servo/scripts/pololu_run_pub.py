import rospy
# from std_msgs.msg import Float32
from ros_pololu_servo.msg import MotorCommand

def interpolate(value, old_min, old_max, new_min, new_max):
    # Width of each range
    old_range = old_max - old_min
    new_range = new_max - new_min

    # Scale old value into range between 0 and 1
    scaled_value = (value - old_min) / old_range

    # Convert the scaled value into the new range
    new_val = new_min + (scaled_value * new_range)

    return new_val

class pololucmd():

    def __init__(self):
        self.motor_pub = rospy.Publisher('pololu/command', MotorCommand, queue_size = 1)


        #setup motor command
        self.cmd = MotorCommand()
        self.cmd.joint_name = 'jaw_joint'
        self.cmd.speed = 1.0
        self.cmd.acceleration = 1.0

        self.max_range = 2000
        interpolate(0.7, 0.0,1.0, 0.0, self.max_range)
        self.motor_pub.publish(self.cmd)

if __name__ == "__main__":
    rospy.init_node('run_pololu')
    rp = pololucmd()
    rospy.spin()