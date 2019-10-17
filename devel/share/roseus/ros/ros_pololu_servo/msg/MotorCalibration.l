;; Auto-generated. Do not edit!


(when (boundp 'ros_pololu_servo::MotorCalibration)
  (if (not (find-package "ROS_POLOLU_SERVO"))
    (make-package "ROS_POLOLU_SERVO"))
  (shadow 'MotorCalibration (find-package "ROS_POLOLU_SERVO")))
(unless (find-package "ROS_POLOLU_SERVO::MOTORCALIBRATION")
  (make-package "ROS_POLOLU_SERVO::MOTORCALIBRATION"))

(in-package "ROS")
;;//! \htmlinclude MotorCalibration.msg.html


(defclass ros_pololu_servo::MotorCalibration
  :super ros::object
  :slots (_min_pulse _min_radians _min_degrees _max_pulse _max_radians _max_degrees ))

(defmethod ros_pololu_servo::MotorCalibration
  (:init
   (&key
    ((:min_pulse __min_pulse) 0)
    ((:min_radians __min_radians) 0.0)
    ((:min_degrees __min_degrees) 0.0)
    ((:max_pulse __max_pulse) 0)
    ((:max_radians __max_radians) 0.0)
    ((:max_degrees __max_degrees) 0.0)
    )
   (send-super :init)
   (setq _min_pulse (round __min_pulse))
   (setq _min_radians (float __min_radians))
   (setq _min_degrees (float __min_degrees))
   (setq _max_pulse (round __max_pulse))
   (setq _max_radians (float __max_radians))
   (setq _max_degrees (float __max_degrees))
   self)
  (:min_pulse
   (&optional __min_pulse)
   (if __min_pulse (setq _min_pulse __min_pulse)) _min_pulse)
  (:min_radians
   (&optional __min_radians)
   (if __min_radians (setq _min_radians __min_radians)) _min_radians)
  (:min_degrees
   (&optional __min_degrees)
   (if __min_degrees (setq _min_degrees __min_degrees)) _min_degrees)
  (:max_pulse
   (&optional __max_pulse)
   (if __max_pulse (setq _max_pulse __max_pulse)) _max_pulse)
  (:max_radians
   (&optional __max_radians)
   (if __max_radians (setq _max_radians __max_radians)) _max_radians)
  (:max_degrees
   (&optional __max_degrees)
   (if __max_degrees (setq _max_degrees __max_degrees)) _max_degrees)
  (:serialization-length
   ()
   (+
    ;; int32 _min_pulse
    4
    ;; float64 _min_radians
    8
    ;; float64 _min_degrees
    8
    ;; int32 _max_pulse
    4
    ;; float64 _max_radians
    8
    ;; float64 _max_degrees
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _min_pulse
       (write-long _min_pulse s)
     ;; float64 _min_radians
       (sys::poke _min_radians (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _min_degrees
       (sys::poke _min_degrees (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int32 _max_pulse
       (write-long _max_pulse s)
     ;; float64 _max_radians
       (sys::poke _max_radians (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _max_degrees
       (sys::poke _max_degrees (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _min_pulse
     (setq _min_pulse (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _min_radians
     (setq _min_radians (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _min_degrees
     (setq _min_degrees (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int32 _max_pulse
     (setq _max_pulse (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _max_radians
     (setq _max_radians (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _max_degrees
     (setq _max_degrees (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get ros_pololu_servo::MotorCalibration :md5sum-) "243cff09419a3549991196c6e5684b74")
(setf (get ros_pololu_servo::MotorCalibration :datatype-) "ros_pololu_servo/MotorCalibration")
(setf (get ros_pololu_servo::MotorCalibration :definition-)
      "int32 min_pulse             # Minimum pwm pulse
float64 min_radians         # Radians corresponding to min pwm pulse
float64 min_degrees         # Degrees corresponding to min pwm pulse
int32 max_pulse             # Maximum pwm pulse
float64 max_radians         # Radians corresponding to max pwm pulse
float64 max_degrees         # Degrees corresponding to max pwm pulse
")



(provide :ros_pololu_servo/MotorCalibration "243cff09419a3549991196c6e5684b74")


