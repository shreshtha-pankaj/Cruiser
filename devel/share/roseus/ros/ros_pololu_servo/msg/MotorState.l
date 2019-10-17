;; Auto-generated. Do not edit!


(when (boundp 'ros_pololu_servo::MotorState)
  (if (not (find-package "ROS_POLOLU_SERVO"))
    (make-package "ROS_POLOLU_SERVO"))
  (shadow 'MotorState (find-package "ROS_POLOLU_SERVO")))
(unless (find-package "ROS_POLOLU_SERVO::MOTORSTATE")
  (make-package "ROS_POLOLU_SERVO::MOTORSTATE"))

(in-package "ROS")
;;//! \htmlinclude MotorState.msg.html


(defclass ros_pololu_servo::MotorState
  :super ros::object
  :slots (_name _pololu_id _motor_id _pulse _radians _degrees _calibration ))

(defmethod ros_pololu_servo::MotorState
  (:init
   (&key
    ((:name __name) "")
    ((:pololu_id __pololu_id) 0)
    ((:motor_id __motor_id) 0)
    ((:pulse __pulse) 0)
    ((:radians __radians) 0.0)
    ((:degrees __degrees) 0.0)
    ((:calibration __calibration) (instance ros_pololu_servo::MotorCalibration :init))
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _pololu_id (round __pololu_id))
   (setq _motor_id (round __motor_id))
   (setq _pulse (round __pulse))
   (setq _radians (float __radians))
   (setq _degrees (float __degrees))
   (setq _calibration __calibration)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:pololu_id
   (&optional __pololu_id)
   (if __pololu_id (setq _pololu_id __pololu_id)) _pololu_id)
  (:motor_id
   (&optional __motor_id)
   (if __motor_id (setq _motor_id __motor_id)) _motor_id)
  (:pulse
   (&optional __pulse)
   (if __pulse (setq _pulse __pulse)) _pulse)
  (:radians
   (&optional __radians)
   (if __radians (setq _radians __radians)) _radians)
  (:degrees
   (&optional __degrees)
   (if __degrees (setq _degrees __degrees)) _degrees)
  (:calibration
   (&rest __calibration)
   (if (keywordp (car __calibration))
       (send* _calibration __calibration)
     (progn
       (if __calibration (setq _calibration (car __calibration)))
       _calibration)))
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; int8 _pololu_id
    1
    ;; int8 _motor_id
    1
    ;; int32 _pulse
    4
    ;; float64 _radians
    8
    ;; float64 _degrees
    8
    ;; ros_pololu_servo/MotorCalibration _calibration
    (send _calibration :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; int8 _pololu_id
       (write-byte _pololu_id s)
     ;; int8 _motor_id
       (write-byte _motor_id s)
     ;; int32 _pulse
       (write-long _pulse s)
     ;; float64 _radians
       (sys::poke _radians (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _degrees
       (sys::poke _degrees (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; ros_pololu_servo/MotorCalibration _calibration
       (send _calibration :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int8 _pololu_id
     (setq _pololu_id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _pololu_id 127) (setq _pololu_id (- _pololu_id 256)))
   ;; int8 _motor_id
     (setq _motor_id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _motor_id 127) (setq _motor_id (- _motor_id 256)))
   ;; int32 _pulse
     (setq _pulse (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _radians
     (setq _radians (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _degrees
     (setq _degrees (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; ros_pololu_servo/MotorCalibration _calibration
     (send _calibration :deserialize buf ptr-) (incf ptr- (send _calibration :serialization-length))
   ;;
   self)
  )

(setf (get ros_pololu_servo::MotorState :md5sum-) "f1e998b21e02fc23ab5efad21cbedab1")
(setf (get ros_pololu_servo::MotorState :datatype-) "ros_pololu_servo/MotorState")
(setf (get ros_pololu_servo::MotorState :definition-)
      "string name                                     # Name of the servo (specified in the yaml file)
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



(provide :ros_pololu_servo/MotorState "f1e998b21e02fc23ab5efad21cbedab1")


