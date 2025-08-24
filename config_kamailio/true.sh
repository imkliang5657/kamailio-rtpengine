#!/bin/bash

# 取得傳入的兩個參數
num1=$1
num2=$2

# 檢查 num1 是否能整除 3
if (( num1 % 3 == 0 )); then
  while true; do
    rand=$((RANDOM % 3))  # 隨機從 0~2 取數
    if [ "$rand" -ne "$num2" ]; then
      echo "$rand"
      break
    fi
  done
else
  echo "false"
fi

