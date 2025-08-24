#!/bin/bash
source counter.txt	
	((msg++))
	msg=$((msg % 3))
	echo $msg
	echo "msg=$msg" >counter.txt
