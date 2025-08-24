#!/bin/bash

# 檢查是否提供了 3 個參數
if [ "$#" -ne 3 ]; then
    echo "使用方式: $0 <id> <num1> <num2>"
    exit 1
fi

# 變數對應
ID=$1
NUM1=$2
NUM2=$3

kamctl db exec "UPDATE rtpengine
SET  $NUM1 = '$NUM2' 
WHERE setid = '$ID';"

