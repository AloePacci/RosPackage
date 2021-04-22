;; Auto-generated. Do not edit!


(when (boundp 'planner::GoTo)
  (if (not (find-package "PLANNER"))
    (make-package "PLANNER"))
  (shadow 'GoTo (find-package "PLANNER")))
(unless (find-package "PLANNER::GOTO")
  (make-package "PLANNER::GOTO"))
(unless (find-package "PLANNER::GOTOREQUEST")
  (make-package "PLANNER::GOTOREQUEST"))
(unless (find-package "PLANNER::GOTORESPONSE")
  (make-package "PLANNER::GOTORESPONSE"))

(in-package "ROS")





(defclass planner::GoToRequest
  :super ros::object
  :slots (_x _y _dist_tolerance ))

(defmethod planner::GoToRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:dist_tolerance __dist_tolerance) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _dist_tolerance (float __dist_tolerance))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:dist_tolerance
   (&optional __dist_tolerance)
   (if __dist_tolerance (setq _dist_tolerance __dist_tolerance)) _dist_tolerance)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _dist_tolerance
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
     ;; float32 _dist_tolerance
       (sys::poke _dist_tolerance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _dist_tolerance
     (setq _dist_tolerance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass planner::GoToResponse
  :super ros::object
  :slots (_success ))

(defmethod planner::GoToResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass planner::GoTo
  :super ros::object
  :slots ())

(setf (get planner::GoTo :md5sum-) "2dfe331712db6ce37561cc7498574abd")
(setf (get planner::GoTo :datatype-) "planner/GoTo")
(setf (get planner::GoTo :request) planner::GoToRequest)
(setf (get planner::GoTo :response) planner::GoToResponse)

(defmethod planner::GoToRequest
  (:response () (instance planner::GoToResponse :init)))

(setf (get planner::GoToRequest :md5sum-) "2dfe331712db6ce37561cc7498574abd")
(setf (get planner::GoToRequest :datatype-) "planner/GoToRequest")
(setf (get planner::GoToRequest :definition-)
      "float32 x
float32 y
float32 dist_tolerance
---
bool success

")

(setf (get planner::GoToResponse :md5sum-) "2dfe331712db6ce37561cc7498574abd")
(setf (get planner::GoToResponse :datatype-) "planner/GoToResponse")
(setf (get planner::GoToResponse :definition-)
      "float32 x
float32 y
float32 dist_tolerance
---
bool success

")



(provide :planner/GoTo "2dfe331712db6ce37561cc7498574abd")


