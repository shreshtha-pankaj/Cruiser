// Auto-generated. Do not edit!

// (in-package ros_pololu_servo.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class MotorRangeRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.motor_name = null;
    }
    else {
      if (initObj.hasOwnProperty('motor_name')) {
        this.motor_name = initObj.motor_name
      }
      else {
        this.motor_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotorRangeRequest
    // Serialize message field [motor_name]
    bufferOffset = _serializer.string(obj.motor_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotorRangeRequest
    let len;
    let data = new MotorRangeRequest(null);
    // Deserialize message field [motor_name]
    data.motor_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.motor_name.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_pololu_servo/MotorRangeRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ea6f8ac7c07fc33a72a46dab1cefc8d1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string motor_name
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MotorRangeRequest(null);
    if (msg.motor_name !== undefined) {
      resolved.motor_name = msg.motor_name;
    }
    else {
      resolved.motor_name = ''
    }

    return resolved;
    }
};

class MotorRangeResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.min = null;
      this.max = null;
      this.direction = null;
    }
    else {
      if (initObj.hasOwnProperty('min')) {
        this.min = initObj.min
      }
      else {
        this.min = 0.0;
      }
      if (initObj.hasOwnProperty('max')) {
        this.max = initObj.max
      }
      else {
        this.max = 0.0;
      }
      if (initObj.hasOwnProperty('direction')) {
        this.direction = initObj.direction
      }
      else {
        this.direction = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MotorRangeResponse
    // Serialize message field [min]
    bufferOffset = _serializer.float32(obj.min, buffer, bufferOffset);
    // Serialize message field [max]
    bufferOffset = _serializer.float32(obj.max, buffer, bufferOffset);
    // Serialize message field [direction]
    bufferOffset = _serializer.float32(obj.direction, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MotorRangeResponse
    let len;
    let data = new MotorRangeResponse(null);
    // Deserialize message field [min]
    data.min = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [max]
    data.max = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [direction]
    data.direction = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_pololu_servo/MotorRangeResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5892eecaa7e34e1c77e0bea237d5e235';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 min
    float32 max
    float32 direction
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MotorRangeResponse(null);
    if (msg.min !== undefined) {
      resolved.min = msg.min;
    }
    else {
      resolved.min = 0.0
    }

    if (msg.max !== undefined) {
      resolved.max = msg.max;
    }
    else {
      resolved.max = 0.0
    }

    if (msg.direction !== undefined) {
      resolved.direction = msg.direction;
    }
    else {
      resolved.direction = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: MotorRangeRequest,
  Response: MotorRangeResponse,
  md5sum() { return '0b4ebe151eea7b75e7c5e34c339aa609'; },
  datatype() { return 'ros_pololu_servo/MotorRange'; }
};
