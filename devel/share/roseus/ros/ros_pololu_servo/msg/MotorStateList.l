;; Auto-generated. Do not edit!


(when (boundp 'ros_pololu_servo::MotorStateList)
  (if (not (find-package "ROS_POLOLU_SERVO"))
    (make-package "ROS_POLOLU_SERVO"))
  (shadow 'MotorStateList (find-package "ROS_POLOLU_SERVO")))
(unless (find-package "ROS_POLOLU_SERVO::MOTORSTATELIST")
  (make-package "ROS_POLOLU_SERVO::MOTORSTATELIST"))

(in-package "ROS")
;;//! \htmlinclude MotorStateList.msg.html


(defclass ros_pololu_servo::MotorStateList
  :super ros::object
  :slots (_motor_states ))

(defmethod ros_pololu_servo::MotorStateList
  (:init
   (&key
    ((:motor_states __motor_states) (let (r) (dotimes (i 0) (push (instance ros_pololu_servo::MotorState :init) r)) r))
    )
   (send-super :init)
   (setq _motor_states __motor_states)
   self)
  (:motor_states
   (&rest __motor_states)
   (if (keywordp (car __motor_states))
       (send* _motor_states __motor_states)
     (progn
       (if __motor_states (setq _motor_states (car __motor_states)))
       _motor_states)))
  (:serialization-length
   ()
   (+
    ;; ros_pololu_servo/MotorState[] _motor_states
    (apply #'+ (send-all _motor_states :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; ros_pololu_servo/MotorState[] _motor_states
     (write-long (length _motor_states) s)
     (dolist (elem _motor_states)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; ros_pololu_servo/MotorState[] _motor_states
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _motor_states (let (r) (dotimes (i n) (push (instance ros_pololu_servo::MotorState :init) r)) r))
     (dolist (elem- _motor_states)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ros_pololu_servo::MotorStateList :md5sum-) "f59501f919a1edaba3d8a1c194971202")
(setf (get ros_pololu_servo::MotorStateList :datatype-) "ros_pololu_servo/MotorStateList")
(setf (get ros_pololu_servo::MotorStateList :definition-)
      "ros_pololu_servo/MotorState[] motor_states

================================================================================
MSG: ros_pololu_servo/MotorState
string name                                     # Name of the servo (specified in the yaml file)
int8 pololu_id                                  # id of the Pololu board (12 by default)
int8 motor_id                                   # id of the servo on the Pololu board
int32 pulse                                     # Pwm servo pulse
float64 radians                                 # Current position of the servo in radians
float64 degrees                                 # Current position of the servo in degrees
ros_pololu_servo/MotorCalibration calibration   # Servo calibration
================================================================================
MSG: ros_pololu_servo/MotorCalibration
int32 min_pulse             # Minimum pwm pulse
float64 min_radians         # Radians corresponding to min pwm pulse
float64 min_degrees         # Degrees corresponding to min pwm pulse
int32 max_pulse             # Maximum pwm pulse
float64 max_radians         # Radians corresponding to max pwm pulse
float64 max_degrees         # Degrees corresponding to max pwm pulse
")



(provide :ros_pololu_servo/MotorStateList "f59501f919a1edaba3d8a1c194971202")


