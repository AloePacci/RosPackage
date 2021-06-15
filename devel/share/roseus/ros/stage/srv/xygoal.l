;; Auto-generated. Do not edit!


(when (boundp 'stage::xygoal)
  (if (not (find-package "STAGE"))
    (make-package "STAGE"))
  (shadow 'xygoal (find-package "STAGE")))
(unless (find-package "STAGE::XYGOAL")
  (make-package "STAGE::XYGOAL"))
(unless (find-package "STAGE::XYGOALREQUEST")
  (make-package "STAGE::XYGOALREQUEST"))
(unless (find-package "STAGE::XYGOALRESPONSE")
  (make-package "STAGE::XYGOALRESPONSE"))

(in-package "ROS")





(defclass stage::xygoalRequest
  :super ros::object
  :slots (_x _y ))

(defmethod stage::xygoalRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass stage::xygoalResponse
  :super ros::object
  :slots (_reach ))

(defmethod stage::xygoalResponse
  (:init
   (&key
    ((:reach __reach) nil)
    )
   (send-super :init)
   (setq _reach __reach)
   self)
  (:reach
   (&optional __reach)
   (if __reach (setq _reach __reach)) _reach)
  (:serialization-length
   ()
   (+
    ;; bool _reach
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _reach
       (if _reach (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _reach
     (setq _reach (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass stage::xygoal
  :super ros::object
  :slots ())

(setf (get stage::xygoal :md5sum-) "d19ef5ce3bf2af44ecc2f565e73d87ee")
(setf (get stage::xygoal :datatype-) "stage/xygoal")
(setf (get stage::xygoal :request) stage::xygoalRequest)
(setf (get stage::xygoal :response) stage::xygoalResponse)

(defmethod stage::xygoalRequest
  (:response () (instance stage::xygoalResponse :init)))

(setf (get stage::xygoalRequest :md5sum-) "d19ef5ce3bf2af44ecc2f565e73d87ee")
(setf (get stage::xygoalRequest :datatype-) "stage/xygoalRequest")
(setf (get stage::xygoalRequest :definition-)
      "float32 x
float32 y
---
bool reach
")

(setf (get stage::xygoalResponse :md5sum-) "d19ef5ce3bf2af44ecc2f565e73d87ee")
(setf (get stage::xygoalResponse :datatype-) "stage/xygoalResponse")
(setf (get stage::xygoalResponse :definition-)
      "float32 x
float32 y
---
bool reach
")



(provide :stage/xygoal "d19ef5ce3bf2af44ecc2f565e73d87ee")

