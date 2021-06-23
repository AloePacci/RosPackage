; Auto-generated. Do not edit!


(cl:in-package stage-srv)


;//! \htmlinclude xygoal-request.msg.html

(cl:defclass <xygoal-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (y
    :reader y
    :initarg :y
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass xygoal-request (<xygoal-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <xygoal-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'xygoal-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name stage-srv:<xygoal-request> is deprecated: use stage-srv:xygoal-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <xygoal-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader stage-srv:x-val is deprecated.  Use stage-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <xygoal-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader stage-srv:y-val is deprecated.  Use stage-srv:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <xygoal-request>) ostream)
  "Serializes a message object of type '<xygoal-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'x))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'y))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <xygoal-request>) istream)
  "Deserializes a message object of type '<xygoal-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'x) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'x)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'y) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'y)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<xygoal-request>)))
  "Returns string type for a service object of type '<xygoal-request>"
  "stage/xygoalRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'xygoal-request)))
  "Returns string type for a service object of type 'xygoal-request"
  "stage/xygoalRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<xygoal-request>)))
  "Returns md5sum for a message object of type '<xygoal-request>"
  "8cd126f9c228a58c5310ae0dba804564")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'xygoal-request)))
  "Returns md5sum for a message object of type 'xygoal-request"
  "8cd126f9c228a58c5310ae0dba804564")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<xygoal-request>)))
  "Returns full string definition for message of type '<xygoal-request>"
  (cl:format cl:nil "float32[] x~%float32[] y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'xygoal-request)))
  "Returns full string definition for message of type 'xygoal-request"
  (cl:format cl:nil "float32[] x~%float32[] y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <xygoal-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'x) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'y) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <xygoal-request>))
  "Converts a ROS message object to a list"
  (cl:list 'xygoal-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
;//! \htmlinclude xygoal-response.msg.html

(cl:defclass <xygoal-response> (roslisp-msg-protocol:ros-message)
  ((reach
    :reader reach
    :initarg :reach
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass xygoal-response (<xygoal-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <xygoal-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'xygoal-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name stage-srv:<xygoal-response> is deprecated: use stage-srv:xygoal-response instead.")))

(cl:ensure-generic-function 'reach-val :lambda-list '(m))
(cl:defmethod reach-val ((m <xygoal-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader stage-srv:reach-val is deprecated.  Use stage-srv:reach instead.")
  (reach m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <xygoal-response>) ostream)
  "Serializes a message object of type '<xygoal-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'reach) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <xygoal-response>) istream)
  "Deserializes a message object of type '<xygoal-response>"
    (cl:setf (cl:slot-value msg 'reach) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<xygoal-response>)))
  "Returns string type for a service object of type '<xygoal-response>"
  "stage/xygoalResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'xygoal-response)))
  "Returns string type for a service object of type 'xygoal-response"
  "stage/xygoalResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<xygoal-response>)))
  "Returns md5sum for a message object of type '<xygoal-response>"
  "8cd126f9c228a58c5310ae0dba804564")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'xygoal-response)))
  "Returns md5sum for a message object of type 'xygoal-response"
  "8cd126f9c228a58c5310ae0dba804564")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<xygoal-response>)))
  "Returns full string definition for message of type '<xygoal-response>"
  (cl:format cl:nil "bool reach~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'xygoal-response)))
  "Returns full string definition for message of type 'xygoal-response"
  (cl:format cl:nil "bool reach~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <xygoal-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <xygoal-response>))
  "Converts a ROS message object to a list"
  (cl:list 'xygoal-response
    (cl:cons ':reach (reach msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'xygoal)))
  'xygoal-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'xygoal)))
  'xygoal-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'xygoal)))
  "Returns string type for a service object of type '<xygoal>"
  "stage/xygoal")