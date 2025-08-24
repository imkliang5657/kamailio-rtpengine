#!/bin/bash

# 指定輸入檔案
INPUT_FILE="/etc/kamailio/sip_message.txt"

if [ ! -f "$INPUT_FILE" ]; then
    echo "❌ 檔案不存在：$INPUT_FILE"
    exit 1
fi

# 去掉 ^M (CR) 符號，然後擷取空行後的 SDP body
cat "$INPUT_FILE" | tr -d '\r' | awk 'BEGIN {found=0} /^$/ {found=1; next} found'| sed ':a;N;$!ba;s/\n/|/g'
