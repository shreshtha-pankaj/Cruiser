// Auto-generated. Do not edit!

// (in-package ros_pololu_servo.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let MotorCalibration = require('./MotorCalibration.js');

//-----------------------------------------------------------

class MotorState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.name = null;
      this.pololu_id = null;
      this.motor_id = null;
      this.pulse = null;
      this.radians = null;
      this.degrees = null;
      this.calibration = null;
    }
    else {
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
      if (initObj.hasOwnProperty('pololu_id')) {
        this.pololu_id = initObj.pololu_id
      }
      else {
        this.pololu_id = 0;
      }
      if (initObj.hasOwnProperty('motor_id')) {
        this.motor_id = initObj.motor_id
      }
      else {
        this.motor_id = 0;
      }
      if (initObj.hasOwnProperty('pulse')) {
        this.pulse = initObj.pulse
      }
      else {
        this.pulse = 0;
      }
      if (initObj.hasOwnProperty('radians')) {
        this.radians = initObj.radians
      }
      else {
        this.radians = 0.0;
      }
      if (initObj.hasOwnProperty('degrees')) {
        this.degrees = initObj.degrees
      }
      else {
        this.degrees = 0.0;
      }
      if (initObj.hasOwnProperty('calibration')) {
        this.calibration = initObj.calibration
      }
      else {
        this.calibration = new MotorCalibration();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotorState
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [pololu_id]
    bufferOffset = _serializer.int8(obj.pololu_id, buffer, bufferOffset);
    // Serialize message field [motor_id]
    bufferOffset = _serializer.int8(obj.motor_id, buffer, bufferOffset);
    // Serialize message field [pulse]
    bufferOffset = _serializer.int32(obj.pulse, buffer, bufferOffset);
    // Serialize message field [radians]
    bufferOffset = _serializer.float64(obj.radians, buffer, bufferOffset);
    // Serialize message field [degrees]
    bufferOffset = _serializer.float64(obj.degrees, buffer, bufferOffset);
    // Serialize message field [calibration]
    bufferOffset = MotorCalibration.serialize(obj.calibration, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotorState
    let len;
    let data = new MotorState(null);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [pololu_id]
    data.pololu_id = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [motor_id]
    data.motor_id = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [pulse]
    data.pulse = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [radians]
    data.radians = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [degrees]
    data.degrees = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [calibration]
    data.calibration = MotorCalibration.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.name.length;
    return length + 66;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_pololu_servo/MotorState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f1e998b21e02fc23ab5efad21cbedab1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new MotorState(null);
    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.pololu_id !== undefined) {
      resolved.pololu_id = msg.pololu_id;
    }
    else {
      resolved.pololu_id = 0
    }

    if (msg.motor_id !== undefined) {
      resolved.motor_id = msg.motor_id;
    }
    else {
      resolved.motor_id = 0
    }

    if (msg.pulse !== undefined) {
      resolved.pulse = msg.pulse;
    }
    else {
      resolved.pulse = 0
    }

    if (msg.radians !== undefined) {
      resolved.radians = msg.radians;
    }
    else {
      resolved.radians = 0.0
    }

    if (msg.degrees !== undefined) {
      resolved.degrees = msg.degrees;
    }
    else {
      resolved.degrees = 0.0
    }

    if (msg.calibration !== undefined) {
      resolved.calibration = MotorCalibration.Resolve(msg.calibration)
    }
    else {
      resolved.calibration = new MotorCalibration()
    }

    return resolved;
    }
};

module.exports = MotorState;
