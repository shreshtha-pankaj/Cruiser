// Auto-generated. Do not edit!

// (in-package ros_pololu_servo.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class MotorCalibration {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.min_pulse = null;
      this.min_radians = null;
      this.min_degrees = null;
      this.max_pulse = null;
      this.max_radians = null;
      this.max_degrees = null;
    }
    else {
      if (initObj.hasOwnProperty('min_pulse')) {
        this.min_pulse = initObj.min_pulse
      }
      else {
        this.min_pulse = 0;
      }
      if (initObj.hasOwnProperty('min_radians')) {
        this.min_radians = initObj.min_radians
      }
      else {
        this.min_radians = 0.0;
      }
      if (initObj.hasOwnProperty('min_degrees')) {
        this.min_degrees = initObj.min_degrees
      }
      else {
        this.min_degrees = 0.0;
      }
      if (initObj.hasOwnProperty('max_pulse')) {
        this.max_pulse = initObj.max_pulse
      }
      else {
        this.max_pulse = 0;
      }
      if (initObj.hasOwnProperty('max_radians')) {
        this.max_radians = initObj.max_radians
      }
      else {
        this.max_radians = 0.0;
      }
      if (initObj.hasOwnProperty('max_degrees')) {
        this.max_degrees = initObj.max_degrees
      }
      else {
        this.max_degrees = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotorCalibration
    // Serialize message field [min_pulse]
    bufferOffset = _serializer.int32(obj.min_pulse, buffer, bufferOffset);
    // Serialize message field [min_radians]
    bufferOffset = _serializer.float64(obj.min_radians, buffer, bufferOffset);
    // Serialize message field [min_degrees]
    bufferOffset = _serializer.float64(obj.min_degrees, buffer, bufferOffset);
    // Serialize message field [max_pulse]
    bufferOffset = _serializer.int32(obj.max_pulse, buffer, bufferOffset);
    // Serialize message field [max_radians]
    bufferOffset = _serializer.float64(obj.max_radians, buffer, bufferOffset);
    // Serialize message field [max_degrees]
    bufferOffset = _serializer.float64(obj.max_degrees, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotorCalibration
    let len;
    let data = new MotorCalibration(null);
    // Deserialize message field [min_pulse]
    data.min_pulse = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [min_radians]
    data.min_radians = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [min_degrees]
    data.min_degrees = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [max_pulse]
    data.max_pulse = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [max_radians]
    data.max_radians = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [max_degrees]
    data.max_degrees = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 40;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_pololu_servo/MotorCalibration';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '243cff09419a3549991196c6e5684b74';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new MotorCalibration(null);
    if (msg.min_pulse !== undefined) {
      resolved.min_pulse = msg.min_pulse;
    }
    else {
      resolved.min_pulse = 0
    }

    if (msg.min_radians !== undefined) {
      resolved.min_radians = msg.min_radians;
    }
    else {
      resolved.min_radians = 0.0
    }

    if (msg.min_degrees !== undefined) {
      resolved.min_degrees = msg.min_degrees;
    }
    else {
      resolved.min_degrees = 0.0
    }

    if (msg.max_pulse !== undefined) {
      resolved.max_pulse = msg.max_pulse;
    }
    else {
      resolved.max_pulse = 0
    }

    if (msg.max_radians !== undefined) {
      resolved.max_radians = msg.max_radians;
    }
    else {
      resolved.max_radians = 0.0
    }

    if (msg.max_degrees !== undefined) {
      resolved.max_degrees = msg.max_degrees;
    }
    else {
      resolved.max_degrees = 0.0
    }

    return resolved;
    }
};

module.exports = MotorCalibration;
