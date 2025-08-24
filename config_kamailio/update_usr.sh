#!/bin/bash

# 檢查是否提供了 3 個參數
if [ "$#" -ne 3 ]; then
    echo "使用方式: $0 <id> <num1> <num2>"
    exit 1
fi

# 變數對應
NUM1=$1
NUM2=$2
NAME=$3

kamctl db exec "UPDATE subscriber
SET   $NUM1 = '$NUM2' 
WHERE username = '$NAME';"
