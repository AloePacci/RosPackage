;; Auto-generated. Do not edit!


(when (boundp 'turtle_pid_control::xygoal)
  (if (not (find-package "TURTLE_PID_CONTROL"))
    (make-package "TURTLE_PID_CONTROL"))
  (shadow 'xygoal (find-package "TURTLE_PID_CONTROL")))
(unless (find-package "TURTLE_PID_CONTROL::XYGOAL")
  (make-package "TURTLE_PID_CONTROL::XYGOAL"))
(unless (find-package "TURTLE_PID_CONTROL::XYGOALREQUEST")
  (make-package "TURTLE_PID_CONTROL::XYGOALREQUEST"))
(unless (find-package "TURTLE_PID_CONTROL::XYGOALRESPONSE")
  (make-package "TURTLE_PID_CONTROL::XYGOALRESPONSE"))

(in-package "ROS")





(defclass turtle_pid_control::xygoalRequest
  :super ros::object
  :slots (_x _y ))

(defmethod turtle_pid_control::xygoalRequest
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

(defclass turtle_pid_control::xygoalResponse
  :super ros::object
  :slots (_reach ))

(defmethod turtle_pid_control::xygoalResponse
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

(defclass turtle_pid_control::xygoal
  :super ros::object
  :slots ())

(setf (get turtle_pid_control::xygoal :md5sum-) "d19ef5ce3bf2af44ecc2f565e73d87ee")
(setf (get turtle_pid_control::xygoal :datatype-) "turtle_pid_control/xygoal")
(setf (get turtle_pid_control::xygoal :request) turtle_pid_control::xygoalRequest)
(setf (get turtle_pid_control::xygoal :response) turtle_pid_control::xygoalResponse)

(defmethod turtle_pid_control::xygoalRequest
  (:response () (instance turtle_pid_control::xygoalResponse :init)))

(setf (get turtle_pid_control::xygoalRequest :md5sum-) "d19ef5ce3bf2af44ecc2f565e73d87ee")
(setf (get turtle_pid_control::xygoalRequest :datatype-) "turtle_pid_control/xygoalRequest")
(setf (get turtle_pid_control::xygoalRequest :definition-)
      "float32 x
float32 y
---
bool reach
")

(setf (get turtle_pid_control::xygoalResponse :md5sum-) "d19ef5ce3bf2af44ecc2f565e73d87ee")
(setf (get turtle_pid_control::xygoalResponse :datatype-) "turtle_pid_control/xygoalResponse")
(setf (get turtle_pid_control::xygoalResponse :definition-)
      "float32 x
float32 y
---
bool reach
")



(provide :turtle_pid_control/xygoal "d19ef5ce3bf2af44ecc2f565e73d87ee")


