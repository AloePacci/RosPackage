; Auto-generated. Do not edit!


(cl:in-package planner-srv)


;//! \htmlinclude GoTo-request.msg.html

(cl:defclass <GoTo-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (dist_tolerance
    :reader dist_tolerance
    :initarg :dist_tolerance
    :type cl:float
    :initform 0.0))
)

(cl:defclass GoTo-request (<GoTo-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GoTo-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GoTo-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name planner-srv:<GoTo-request> is deprecated: use planner-srv:GoTo-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <GoTo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planner-srv:x-val is deprecated.  Use planner-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <GoTo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planner-srv:y-val is deprecated.  Use planner-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'dist_tolerance-val :lambda-list '(m))
(cl:defmethod dist_tolerance-val ((m <GoTo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planner-srv:dist_tolerance-val is deprecated.  Use planner-srv:dist_tolerance instead.")
  (dist_tolerance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GoTo-request>) ostream)
  "Serializes a message object of type '<GoTo-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dist_tolerance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GoTo-request>) istream)
  "Deserializes a message object of type '<GoTo-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dist_tolerance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GoTo-request>)))
  "Returns string type for a service object of type '<GoTo-request>"
  "planner/GoToRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoTo-request)))
  "Returns string type for a service object of type 'GoTo-request"
  "planner/GoToRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GoTo-request>)))
  "Returns md5sum for a message object of type '<GoTo-request>"
  "2dfe331712db6ce37561cc7498574abd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GoTo-request)))
  "Returns md5sum for a message object of type 'GoTo-request"
  "2dfe331712db6ce37561cc7498574abd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GoTo-request>)))
  "Returns full string definition for message of type '<GoTo-request>"
  (cl:format cl:nil "float32 x~%float32 y~%float32 dist_tolerance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GoTo-request)))
  "Returns full string definition for message of type 'GoTo-request"
  (cl:format cl:nil "float32 x~%float32 y~%float32 dist_tolerance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GoTo-request>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GoTo-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GoTo-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':dist_tolerance (dist_tolerance msg))
))
;//! \htmlinclude GoTo-response.msg.html

(cl:defclass <GoTo-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GoTo-response (<GoTo-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GoTo-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GoTo-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name planner-srv:<GoTo-response> is deprecated: use planner-srv:GoTo-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <GoTo-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader planner-srv:success-val is deprecated.  Use planner-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GoTo-response>) ostream)
  "Serializes a message object of type '<GoTo-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GoTo-response>) istream)
  "Deserializes a message object of type '<GoTo-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GoTo-response>)))
  "Returns string type for a service object of type '<GoTo-response>"
  "planner/GoToResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoTo-response)))
  "Returns string type for a service object of type 'GoTo-response"
  "planner/GoToResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GoTo-response>)))
  "Returns md5sum for a message object of type '<GoTo-response>"
  "2dfe331712db6ce37561cc7498574abd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GoTo-response)))
  "Returns md5sum for a message object of type 'GoTo-response"
  "2dfe331712db6ce37561cc7498574abd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GoTo-response>)))
  "Returns full string definition for message of type '<GoTo-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GoTo-response)))
  "Returns full string definition for message of type 'GoTo-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GoTo-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GoTo-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GoTo-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GoTo)))
  'GoTo-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GoTo)))
  'GoTo-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoTo)))
  "Returns string type for a service object of type '<GoTo>"
  "planner/GoTo")