#!/bin/bash

cmd=$1
userName=hduser
passWord=artha
fileName=./cluster
totalLines=`cat ${fileName} | wc -l`

for (( z=1 ; z<=${totalLines} ; z++))
do
	echo ""
	echo ${z}"." "ssh on ip address" `sed -n ${z}p ${fileName}` ", command:" ${cmd}
	sshpass -p ${passWord} ssh -o StrictHostKeyChecking=no ${userName}@`sed -n ${z}p ${fileName}` ${cmd}
done
