;; Auto-generated. Do not edit!


(when (boundp 'ros_pololu_servo::MotorCommand)
  (if (not (find-package "ROS_POLOLU_SERVO"))
    (make-package "ROS_POLOLU_SERVO"))
  (shadow 'MotorCommand (find-package "ROS_POLOLU_SERVO")))
(unless (find-package "ROS_POLOLU_SERVO::MOTORCOMMAND")
  (make-package "ROS_POLOLU_SERVO::MOTORCOMMAND"))

(in-package "ROS")
;;//! \htmlinclude MotorCommand.msg.html


(defclass ros_pololu_servo::MotorCommand
  :super ros::object
  :slots (_joint_name _position _speed _acceleration ))

(defmethod ros_pololu_servo::MotorCommand
  (:init
   (&key
    ((:joint_name __joint_name) "")
    ((:position __position) 0.0)
    ((:speed __speed) 0.0)
    ((:acceleration __acceleration) 0.0)
    )
   (send-super :init)
   (setq _joint_name (string __joint_name))
   (setq _position (float __position))
   (setq _speed (float __speed))
   (setq _acceleration (float __acceleration))
   self)
  (:joint_name
   (&optional __joint_name)
   (if __joint_name (setq _joint_name __joint_name)) _joint_name)
  (:position
   (&optional __position)
   (if __position (setq _position __position)) _position)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:acceleration
   (&optional __acceleration)
   (if __acceleration (setq _acceleration __acceleration)) _acceleration)
  (:serialization-length
   ()
   (+
    ;; string _joint_name
    4 (length _joint_name)
    ;; float64 _position
    8
    ;; float32 _speed
    4
    ;; float32 _acceleration
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _joint_name
       (write-long (length _joint_name) s) (princ _joint_name s)
     ;; float64 _position
       (sys::poke _position (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _acceleration
       (sys::poke _acceleration (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _joint_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _joint_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _position
     (setq _position (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _acceleration
     (setq _acceleration (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get ros_pololu_servo::MotorCommand :md5sum-) "c357daac337dac3f7e4bb73a055e6e8c")
(setf (get ros_pololu_servo::MotorCommand :datatype-) "ros_pololu_servo/MotorCommand")
(setf (get ros_pololu_servo::MotorCommand :definition-)
      "string joint_name       # Name of the joint (specified in the yaml file), or motor_id for default calibration
float64 position        # Position to move to in radians
float32 speed           # Speed to move at (0.0 - 1.0)
float32 acceleration    # Acceleration to move at (0.0 - 1.0)

")



(provide :ros_pololu_servo/MotorCommand "c357daac337dac3f7e4bb73a055e6e8c")


