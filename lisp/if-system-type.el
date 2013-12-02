
(if (eq system-type 'gnu/linux)
    (message "This is linux")
  (message "This is not linux"))


(if (eq system-type 'windows-nt)
    (message "This is windows")
  (message "This is not windows"))

