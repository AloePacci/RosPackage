// Auto-generated. Do not edit!

// (in-package stage.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class xygoalRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = [];
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type xygoalRequest
    // Serialize message field [x]
    bufferOffset = _arraySerializer.float32(obj.x, buffer, bufferOffset, null);
    // Serialize message field [y]
    bufferOffset = _arraySerializer.float32(obj.y, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type xygoalRequest
    let len;
    let data = new xygoalRequest(null);
    // Deserialize message field [x]
    data.x = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [y]
    data.y = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.x.length;
    length += 4 * object.y.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'stage/xygoalRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '462ac0ba687f22c2e73c0ec0413e0202';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] x
    float32[] y
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new xygoalRequest(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = []
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = []
    }

    return resolved;
    }
};

class xygoalResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.reach = null;
    }
    else {
      if (initObj.hasOwnProperty('reach')) {
        this.reach = initObj.reach
      }
      else {
        this.reach = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type xygoalResponse
    // Serialize message field [reach]
    bufferOffset = _serializer.bool(obj.reach, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type xygoalResponse
    let len;
    let data = new xygoalResponse(null);
    // Deserialize message field [reach]
    data.reach = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'stage/xygoalResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e28478de0c42bf45c139fda1fb68c47f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool reach
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new xygoalResponse(null);
    if (msg.reach !== undefined) {
      resolved.reach = msg.reach;
    }
    else {
      resolved.reach = false
    }

    return resolved;
    }
};

module.exports = {
  Request: xygoalRequest,
  Response: xygoalResponse,
  md5sum() { return '8cd126f9c228a58c5310ae0dba804564'; },
  datatype() { return 'stage/xygoal'; }
};
