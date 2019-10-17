
(cl:in-package :asdf)

(defsystem "ros_pololu_servo-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
               :trajectory_msgs-msg
)
  :components ((:file "_package")
    (:file "MotorCalibration" :depends-on ("_package_MotorCalibration"))
    (:file "_package_MotorCalibration" :depends-on ("_package"))
    (:file "MotorCommand" :depends-on ("_package_MotorCommand"))
    (:file "_package_MotorCommand" :depends-on ("_package"))
    (:file "MotorState" :depends-on ("_package_MotorState"))
    (:file "_package_MotorState" :depends-on ("_package"))
    (:file "MotorStateList" :depends-on ("_package_MotorStateList"))
    (:file "_package_MotorStateList" :depends-on ("_package"))
    (:file "pololu_trajectoryAction" :depends-on ("_package_pololu_trajectoryAction"))
    (:file "_package_pololu_trajectoryAction" :depends-on ("_package"))
    (:file "pololu_trajectoryActionFeedback" :depends-on ("_package_pololu_trajectoryActionFeedback"))
    (:file "_package_pololu_trajectoryActionFeedback" :depends-on ("_package"))
    (:file "pololu_trajectoryActionGoal" :depends-on ("_package_pololu_trajectoryActionGoal"))
    (:file "_package_pololu_trajectoryActionGoal" :depends-on ("_package"))
    (:file "pololu_trajectoryActionResult" :depends-on ("_package_pololu_trajectoryActionResult"))
    (:file "_package_pololu_trajectoryActionResult" :depends-on ("_package"))
    (:file "pololu_trajectoryFeedback" :depends-on ("_package_pololu_trajectoryFeedback"))
    (:file "_package_pololu_trajectoryFeedback" :depends-on ("_package"))
    (:file "pololu_trajectoryGoal" :depends-on ("_package_pololu_trajectoryGoal"))
    (:file "_package_pololu_trajectoryGoal" :depends-on ("_package"))
    (:file "pololu_trajectoryResult" :depends-on ("_package_pololu_trajectoryResult"))
    (:file "_package_pololu_trajectoryResult" :depends-on ("_package"))
  ))