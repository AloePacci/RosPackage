
(cl:in-package :asdf)

(defsystem "stage-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "xygoal" :depends-on ("_package_xygoal"))
    (:file "_package_xygoal" :depends-on ("_package"))
  ))