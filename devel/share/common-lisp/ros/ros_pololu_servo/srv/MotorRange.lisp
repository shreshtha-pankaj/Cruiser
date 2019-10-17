; Auto-generated. Do not edit!


(cl:in-package ros_pololu_servo-srv)


;//! \htmlinclude MotorRange-request.msg.html

(cl:defclass <MotorRange-request> (roslisp-msg-protocol:ros-message)
  ((motor_name
    :reader motor_name
    :initarg :motor_name
    :type cl:string
    :initform ""))
)

(cl:defclass MotorRange-request (<MotorRange-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotorRange-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotorRange-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_pololu_servo-srv:<MotorRange-request> is deprecated: use ros_pololu_servo-srv:MotorRange-request instead.")))

(cl:ensure-generic-function 'motor_name-val :lambda-list '(m))
(cl:defmethod motor_name-val ((m <MotorRange-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-srv:motor_name-val is deprecated.  Use ros_pololu_servo-srv:motor_name instead.")
  (motor_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotorRange-request>) ostream)
  "Serializes a message object of type '<MotorRange-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'motor_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'motor_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotorRange-request>) istream)
  "Deserializes a message object of type '<MotorRange-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motor_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'motor_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotorRange-request>)))
  "Returns string type for a service object of type '<MotorRange-request>"
  "ros_pololu_servo/MotorRangeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotorRange-request)))
  "Returns string type for a service object of type 'MotorRange-request"
  "ros_pololu_servo/MotorRangeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotorRange-request>)))
  "Returns md5sum for a message object of type '<MotorRange-request>"
  "0b4ebe151eea7b75e7c5e34c339aa609")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotorRange-request)))
  "Returns md5sum for a message object of type 'MotorRange-request"
  "0b4ebe151eea7b75e7c5e34c339aa609")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotorRange-request>)))
  "Returns full string definition for message of type '<MotorRange-request>"
  (cl:format cl:nil "string motor_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotorRange-request)))
  "Returns full string definition for message of type 'MotorRange-request"
  (cl:format cl:nil "string motor_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotorRange-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'motor_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotorRange-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MotorRange-request
    (cl:cons ':motor_name (motor_name msg))
))
;//! \htmlinclude MotorRange-response.msg.html

(cl:defclass <MotorRange-response> (roslisp-msg-protocol:ros-message)
  ((min
    :reader min
    :initarg :min
    :type cl:float
    :initform 0.0)
   (max
    :reader max
    :initarg :max
    :type cl:float
    :initform 0.0)
   (direction
    :reader direction
    :initarg :direction
    :type cl:float
    :initform 0.0))
)

(cl:defclass MotorRange-response (<MotorRange-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MotorRange-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MotorRange-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_pololu_servo-srv:<MotorRange-response> is deprecated: use ros_pololu_servo-srv:MotorRange-response instead.")))

(cl:ensure-generic-function 'min-val :lambda-list '(m))
(cl:defmethod min-val ((m <MotorRange-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-srv:min-val is deprecated.  Use ros_pololu_servo-srv:min instead.")
  (min m))

(cl:ensure-generic-function 'max-val :lambda-list '(m))
(cl:defmethod max-val ((m <MotorRange-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-srv:max-val is deprecated.  Use ros_pololu_servo-srv:max instead.")
  (max m))

(cl:ensure-generic-function 'direction-val :lambda-list '(m))
(cl:defmethod direction-val ((m <MotorRange-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_pololu_servo-srv:direction-val is deprecated.  Use ros_pololu_servo-srv:direction instead.")
  (direction m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MotorRange-response>) ostream)
  "Serializes a message object of type '<MotorRange-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'min))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'max))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'direction))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MotorRange-response>) istream)
  "Deserializes a message object of type '<MotorRange-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'min) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'direction) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MotorRange-response>)))
  "Returns string type for a service object of type '<MotorRange-response>"
  "ros_pololu_servo/MotorRangeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotorRange-response)))
  "Returns string type for a service object of type 'MotorRange-response"
  "ros_pololu_servo/MotorRangeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MotorRange-response>)))
  "Returns md5sum for a message object of type '<MotorRange-response>"
  "0b4ebe151eea7b75e7c5e34c339aa609")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MotorRange-response)))
  "Returns md5sum for a message object of type 'MotorRange-response"
  "0b4ebe151eea7b75e7c5e34c339aa609")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MotorRange-response>)))
  "Returns full string definition for message of type '<MotorRange-response>"
  (cl:format cl:nil "float32 min~%float32 max~%float32 direction~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MotorRange-response)))
  "Returns full string definition for message of type 'MotorRange-response"
  (cl:format cl:nil "float32 min~%float32 max~%float32 direction~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MotorRange-response>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MotorRange-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MotorRange-response
    (cl:cons ':min (min msg))
    (cl:cons ':max (max msg))
    (cl:cons ':direction (direction msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MotorRange)))
  'MotorRange-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MotorRange)))
  'MotorRange-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MotorRange)))
  "Returns string type for a service object of type '<MotorRange>"
  "ros_pololu_servo/MotorRange")