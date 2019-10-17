;; Auto-generated. Do not edit!


(when (boundp 'ros_pololu_servo::MotorRange)
  (if (not (find-package "ROS_POLOLU_SERVO"))
    (make-package "ROS_POLOLU_SERVO"))
  (shadow 'MotorRange (find-package "ROS_POLOLU_SERVO")))
(unless (find-package "ROS_POLOLU_SERVO::MOTORRANGE")
  (make-package "ROS_POLOLU_SERVO::MOTORRANGE"))
(unless (find-package "ROS_POLOLU_SERVO::MOTORRANGEREQUEST")
  (make-package "ROS_POLOLU_SERVO::MOTORRANGEREQUEST"))
(unless (find-package "ROS_POLOLU_SERVO::MOTORRANGERESPONSE")
  (make-package "ROS_POLOLU_SERVO::MOTORRANGERESPONSE"))

(in-package "ROS")





(defclass ros_pololu_servo::MotorRangeRequest
  :super ros::object
  :slots (_motor_name ))

(defmethod ros_pololu_servo::MotorRangeRequest
  (:init
   (&key
    ((:motor_name __motor_name) "")
    )
   (send-super :init)
   (setq _motor_name (string __motor_name))
   self)
  (:motor_name
   (&optional __motor_name)
   (if __motor_name (setq _motor_name __motor_name)) _motor_name)
  (:serialization-length
   ()
   (+
    ;; string _motor_name
    4 (length _motor_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _motor_name
       (write-long (length _motor_name) s) (princ _motor_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _motor_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _motor_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass ros_pololu_servo::MotorRangeResponse
  :super ros::object
  :slots (_min _max _direction ))

(defmethod ros_pololu_servo::MotorRangeResponse
  (:init
   (&key
    ((:min __min) 0.0)
    ((:max __max) 0.0)
    ((:direction __direction) 0.0)
    )
   (send-super :init)
   (setq _min (float __min))
   (setq _max (float __max))
   (setq _direction (float __direction))
   self)
  (:min
   (&optional __min)
   (if __min (setq _min __min)) _min)
  (:max
   (&optional __max)
   (if __max (setq _max __max)) _max)
  (:direction
   (&optional __direction)
   (if __direction (setq _direction __direction)) _direction)
  (:serialization-length
   ()
   (+
    ;; float32 _min
    4
    ;; float32 _max
    4
    ;; float32 _direction
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _min
       (sys::poke _min (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _max
       (sys::poke _max (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _direction
       (sys::poke _direction (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _min
     (setq _min (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _max
     (setq _max (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _direction
     (setq _direction (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass ros_pololu_servo::MotorRange
  :super ros::object
  :slots ())

(setf (get ros_pololu_servo::MotorRange :md5sum-) "0b4ebe151eea7b75e7c5e34c339aa609")
(setf (get ros_pololu_servo::MotorRange :datatype-) "ros_pololu_servo/MotorRange")
(setf (get ros_pololu_servo::MotorRange :request) ros_pololu_servo::MotorRangeRequest)
(setf (get ros_pololu_servo::MotorRange :response) ros_pololu_servo::MotorRangeResponse)

(defmethod ros_pololu_servo::MotorRangeRequest
  (:response () (instance ros_pololu_servo::MotorRangeResponse :init)))

(setf (get ros_pololu_servo::MotorRangeRequest :md5sum-) "0b4ebe151eea7b75e7c5e34c339aa609")
(setf (get ros_pololu_servo::MotorRangeRequest :datatype-) "ros_pololu_servo/MotorRangeRequest")
(setf (get ros_pololu_servo::MotorRangeRequest :definition-)
      "string motor_name
---
float32 min
float32 max
float32 direction
")

(setf (get ros_pololu_servo::MotorRangeResponse :md5sum-) "0b4ebe151eea7b75e7c5e34c339aa609")
(setf (get ros_pololu_servo::MotorRangeResponse :datatype-) "ros_pololu_servo/MotorRangeResponse")
(setf (get ros_pololu_servo::MotorRangeResponse :definition-)
      "string motor_name
---
float32 min
float32 max
float32 direction
")



(provide :ros_pololu_servo/MotorRange "0b4ebe151eea7b75e7c5e34c339aa609")


