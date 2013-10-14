#!/bin/bash

# acurl.sh - Auto Curl - Automatically resume interrupted downloads with curl
#
# curl exit codes for interrupted downloads is 18 or 56 and $? gives you that
# code.  so we keep trying to download the same file name [-O] while resuming
# where we left off previously [-C]
#
# Created: 2013-10-13 11:36:01 by Jonas Gorauskas [JGG]
# Modified: 2013-10-14 01:31 by jgg

export ec=1;

while [ $ec -gt 0 ]; do
    /usr/bin/curl -O -C - $1;
    export ec=$?;
done

if [ $ec -eq 0 ]; then
    echo "Downloaded $1";
fi


# TODO the below error code 33 causes the above script to go into an infinite loop.
#
# ** Resuming transfer from byte position 554696704
#   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
#                                  Dload  Upload   Total   Spent    Left  Speed
#   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
# curl: (33) HTTP server doesn't seem to support byte ranges. Cannot resume.
