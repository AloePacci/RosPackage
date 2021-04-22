
(cl:in-package :asdf)

(defsystem "planner-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "GoTo" :depends-on ("_package_GoTo"))
    (:file "_package_GoTo" :depends-on ("_package"))
  ))