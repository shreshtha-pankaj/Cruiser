// Auto-generated. Do not edit!

// (in-package ros_pololu_servo.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let MotorState = require('./MotorState.js');

//-----------------------------------------------------------

class MotorStateList {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.motor_states = null;
    }
    else {
      if (initObj.hasOwnProperty('motor_states')) {
        this.motor_states = initObj.motor_states
      }
      else {
        this.motor_states = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotorStateList
    // Serialize message field [motor_states]
    // Serialize the length for message field [motor_states]
    bufferOffset = _serializer.uint32(obj.motor_states.length, buffer, bufferOffset);
    obj.motor_states.forEach((val) => {
      bufferOffset = MotorState.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotorStateList
    let len;
    let data = new MotorStateList(null);
    // Deserialize message field [motor_states]
    // Deserialize array length for message field [motor_states]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.motor_states = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.motor_states[i] = MotorState.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.motor_states.forEach((val) => {
      length += MotorState.getMessageSize(val);
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_pololu_servo/MotorStateList';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f59501f919a1edaba3d8a1c194971202';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    ros_pololu_servo/MotorState[] motor_states
    
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MotorStateList(null);
    if (msg.motor_states !== undefined) {
      resolved.motor_states = new Array(msg.motor_states.length);
      for (let i = 0; i < resolved.motor_states.length; ++i) {
        resolved.motor_states[i] = MotorState.Resolve(msg.motor_states[i]);
      }
    }
    else {
      resolved.motor_states = []
    }

    return resolved;
    }
};

module.exports = MotorStateList;
