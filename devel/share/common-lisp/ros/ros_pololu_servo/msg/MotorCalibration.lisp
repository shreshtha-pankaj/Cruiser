; Auto-generated. Do not edit!


(cl:in-package ros_pololu_servo-msg)


;//! \htmlinclude MotorCalibration.msg.html

(cl:defclass <MotorCalibration> (roslisp-msg-protocol:ros-message)
  ((min_pulse
    :reader min_pulse
    :initarg :min_pulse
    :type cl:integer
    :initform 0)
   (min_radians
    :reader min_radians
    :initarg :min_radians
    :type cl:float
    :initform 0.0)
   (min_degrees
    :reader min_degrees
    :initarg :min_degrees
    :type cl:float
    :initform 0.0)
   (max_pulse
    :reader max_pulse
    :initarg :max_pulse
    :type cl:integer
    :initform 0)
   (max_radians
    :reader max_radians
    :initarg :max_radians
    :type cl:float
    :initform 0.0)
   (max_degrees
    :reader max_degrees
    :initarg :max_degrees
    :type cl:float
    :initform 0.0))
)

(cl:defclass MotorCalibration (<MotorCalibration>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotorCalibration>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotorCalibration)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_pololu_servo-msg:<MotorCalibration> is deprecated: use ros_pololu_servo-msg:MotorCalibration instead.")))

(cl:ensure-generic-function 'min_pulse-val :lambda-list '(m))
(cl:defmethod min_pulse-val ((m <MotorCalibration>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-msg:min_pulse-val is deprecated.  Use ros_pololu_servo-msg:min_pulse instead.")
  (min_pulse m))

(cl:ensure-generic-function 'min_radians-val :lambda-list '(m))
(cl:defmethod min_radians-val ((m <MotorCalibration>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-msg:min_radians-val is deprecated.  Use ros_pololu_servo-msg:min_radians instead.")
  (min_radians m))

(cl:ensure-generic-function 'min_degrees-val :lambda-list '(m))
(cl:defmethod min_degrees-val ((m <MotorCalibration>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-msg:min_degrees-val is deprecated.  Use ros_pololu_servo-msg:min_degrees instead.")
  (min_degrees m))

(cl:ensure-generic-function 'max_pulse-val :lambda-list '(m))
(cl:defmethod max_pulse-val ((m <MotorCalibration>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-msg:max_pulse-val is deprecated.  Use ros_pololu_servo-msg:max_pulse instead.")
  (max_pulse m))

(cl:ensure-generic-function 'max_radians-val :lambda-list '(m))
(cl:defmethod max_radians-val ((m <MotorCalibration>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-msg:max_radians-val is deprecated.  Use ros_pololu_servo-msg:max_radians instead.")
  (max_radians m))

(cl:ensure-generic-function 'max_degrees-val :lambda-list '(m))
(cl:defmethod max_degrees-val ((m <MotorCalibration>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-msg:max_degrees-val is deprecated.  Use ros_pololu_servo-msg:max_degrees instead.")
  (max_degrees m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotorCalibration>) ostream)
  "Serializes a message object of type '<MotorCalibration>"
  (cl:let* ((signed (cl:slot-value msg 'min_pulse)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'min_radians))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'min_degrees))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'max_pulse)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'max_radians))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'max_degrees))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotorCalibration>) istream)
  "Deserializes a message object of type '<MotorCalibration>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'min_pulse) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'min_radians) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'min_degrees) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'max_pulse) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_radians) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_degrees) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotorCalibration>)))
  "Returns string type for a message object of type '<MotorCalibration>"
  "ros_pololu_servo/MotorCalibration")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotorCalibration)))
  "Returns string type for a message object of type 'MotorCalibration"
  "ros_pololu_servo/MotorCalibration")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotorCalibration>)))
  "Returns md5sum for a message object of type '<MotorCalibration>"
  "243cff09419a3549991196c6e5684b74")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotorCalibration)))
  "Returns md5sum for a message object of type 'MotorCalibration"
  "243cff09419a3549991196c6e5684b74")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotorCalibration>)))
  "Returns full string definition for message of type '<MotorCalibration>"
  (cl:format cl:nil "int32 min_pulse             # Minimum pwm pulse~%float64 min_radians         # Radians corresponding to min pwm pulse~%float64 min_degrees         # Degrees corresponding to min pwm pulse~%int32 max_pulse             # Maximum pwm pulse~%float64 max_radians         # Radians corresponding to max pwm pulse~%float64 max_degrees         # Degrees corresponding to max pwm pulse~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotorCalibration)))
  "Returns full string definition for message of type 'MotorCalibration"
  (cl:format cl:nil "int32 min_pulse             # Minimum pwm pulse~%float64 min_radians         # Radians corresponding to min pwm pulse~%float64 min_degrees         # Degrees corresponding to min pwm pulse~%int32 max_pulse             # Maximum pwm pulse~%float64 max_radians         # Radians corresponding to max pwm pulse~%float64 max_degrees         # Degrees corresponding to max pwm pulse~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotorCalibration>))
  (cl:+ 0
     4
     8
     8
     4
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotorCalibration>))
  "Converts a ROS message object to a list"
  (cl:list 'MotorCalibration
    (cl:cons ':min_pulse (min_pulse msg))
    (cl:cons ':min_radians (min_radians msg))
    (cl:cons ':min_degrees (min_degrees msg))
    (cl:cons ':max_pulse (max_pulse msg))
    (cl:cons ':max_radians (max_radians msg))
    (cl:cons ':max_degrees (max_degrees msg))
))
