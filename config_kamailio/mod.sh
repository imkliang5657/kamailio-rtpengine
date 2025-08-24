#!/bin/bash

# 取得傳入的兩個參數
num1=$1
num2=$2

# 檢查 num1 是否能整除 3
if (( num1 % 3 == 0 )); then
  while true; do
    rand=$((RANDOM % 3))  # 隨機從 0~2 取數
    if [ "$rand" -ne "$num2" ]; then
      echo "隨機數（不等於第二個變數）: $rand"
      break
    fi
  done
else
  echo "第一個變數 $num1 無法整除 3，未執行隨機操作"
fi

