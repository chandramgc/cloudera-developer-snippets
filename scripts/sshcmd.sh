#!/bin/bash

ipId=$1
userName=hduser
passWord=artha
fileName=./cluster

sshpass -p ${passWord} ssh -o StrictHostKeyChecking=no $userName@`sed -n ${ipId}p ${fileName}`
