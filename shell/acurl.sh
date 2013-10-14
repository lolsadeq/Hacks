#!/bin/bash

# acurl.sh - Auto Curl - Automatically resume interrupted downloads with curl
#
# curl exit codes for interrupted downloads is 18 or 56 and $? gives you that
# code.  so we keep trying to download the same file name [-O] while resuming
# where we left off previously [-C]
#
# Created: 2013-10-13 11:36:01 by Jonas Gorauskas [JGG]
# Modified: 2013-10-13 15:32 by jgg

export ec=1;

while [ $ec -gt 0 ];
do
    /usr/bin/curl -O -C - $1;
    export ec=$?;
done

if [ $ec -eq 0 ];
    echo "Downloaded $1";
fi
