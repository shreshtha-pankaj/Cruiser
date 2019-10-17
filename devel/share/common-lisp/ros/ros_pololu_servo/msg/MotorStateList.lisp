; Auto-generated. Do not edit!


(cl:in-package ros_pololu_servo-msg)


;//! \htmlinclude MotorStateList.msg.html

(cl:defclass <MotorStateList> (roslisp-msg-protocol:ros-message)
  ((motor_states
    :reader motor_states
    :initarg :motor_states
    :type (cl:vector ros_pololu_servo-msg:MotorState)
   :initform (cl:make-array 0 :element-type 'ros_pololu_servo-msg:MotorState :initial-element (cl:make-instance 'ros_pololu_servo-msg:MotorState))))
)

(cl:defclass MotorStateList (<MotorStateList>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotorStateList>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotorStateList)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_pololu_servo-msg:<MotorStateList> is deprecated: use ros_pololu_servo-msg:MotorStateList instead.")))

(cl:ensure-generic-function 'motor_states-val :lambda-list '(m))
(cl:defmethod motor_states-val ((m <MotorStateList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-msg:motor_states-val is deprecated.  Use ros_pololu_servo-msg:motor_states instead.")
  (motor_states m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotorStateList>) ostream)
  "Serializes a message object of type '<MotorStateList>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'motor_states))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'motor_states))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotorStateList>) istream)
  "Deserializes a message object of type '<MotorStateList>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'motor_states) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'motor_states)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'ros_pololu_servo-msg:MotorState))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotorStateList>)))
  "Returns string type for a message object of type '<MotorStateList>"
  "ros_pololu_servo/MotorStateList")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotorStateList)))
  "Returns string type for a message object of type 'MotorStateList"
  "ros_pololu_servo/MotorStateList")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotorStateList>)))
  "Returns md5sum for a message object of type '<MotorStateList>"
  "f59501f919a1edaba3d8a1c194971202")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotorStateList)))
  "Returns md5sum for a message object of type 'MotorStateList"
  "f59501f919a1edaba3d8a1c194971202")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotorStateList>)))
  "Returns full string definition for message of type '<MotorStateList>"
  (cl:format cl:nil "ros_pololu_servo/MotorState[] motor_states~%~%================================================================================~%MSG: ros_pololu_servo/MotorState~%string name                                     # Name of the servo (specified in the yaml file)~%int8 pololu_id                                  # id of the Pololu board (12 by default)~%int8 motor_id                                   # id of the servo on the Pololu board~%int32 pulse                                     # Pwm servo pulse~%float64 radians                                 # Current position of the servo in radians~%float64 degrees                                 # Current position of the servo in degrees~%ros_pololu_servo/MotorCalibration calibration   # Servo calibration~%================================================================================~%MSG: ros_pololu_servo/MotorCalibration~%int32 min_pulse             # Minimum pwm pulse~%float64 min_radians         # Radians corresponding to min pwm pulse~%float64 min_degrees         # Degrees corresponding to min pwm pulse~%int32 max_pulse             # Maximum pwm pulse~%float64 max_radians         # Radians corresponding to max pwm pulse~%float64 max_degrees         # Degrees corresponding to max pwm pulse~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotorStateList)))
  "Returns full string definition for message of type 'MotorStateList"
  (cl:format cl:nil "ros_pololu_servo/MotorState[] motor_states~%~%================================================================================~%MSG: ros_pololu_servo/MotorState~%string name                                     # Name of the servo (specified in the yaml file)~%int8 pololu_id                                  # id of the Pololu board (12 by default)~%int8 motor_id                                   # id of the servo on the Pololu board~%int32 pulse                                     # Pwm servo pulse~%float64 radians                                 # Current position of the servo in radians~%float64 degrees                                 # Current position of the servo in degrees~%ros_pololu_servo/MotorCalibration calibration   # Servo calibration~%================================================================================~%MSG: ros_pololu_servo/MotorCalibration~%int32 min_pulse             # Minimum pwm pulse~%float64 min_radians         # Radians corresponding to min pwm pulse~%float64 min_degrees         # Degrees corresponding to min pwm pulse~%int32 max_pulse             # Maximum pwm pulse~%float64 max_radians         # Radians corresponding to max pwm pulse~%float64 max_degrees         # Degrees corresponding to max pwm pulse~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotorStateList>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'motor_states) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotorStateList>))
  "Converts a ROS message object to a list"
  (cl:list 'MotorStateList
    (cl:cons ':motor_states (motor_states msg))
))
