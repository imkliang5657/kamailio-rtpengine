import bencodepy
import socket
import json
def beautify_bytes_dict(d):
    if isinstance(d, dict):
        return {beautify_bytes_dict(k): beautify_bytes_dict(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [beautify_bytes_dict(i) for i in d]
    elif isinstance(d, bytes):
        try:
            return d.decode('utf-8')
        except:
            return str(d)
    else:
        return d

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('114.35.197.224', 12223)

cookie = b"0_2393_6"
payload = bencodepy.encode({b'command': b'list'})
message = cookie + b' ' + payload

print("Sending:", message)

# 傳送請求
sock.sendto(message, server_address)

print('waiting to receive')
data, server = sock.recvfrom(4096)

# 解析回應
print('received:', data)
cookie, payload = data.split(b' ', 1)
decoded = bencodepy.decode(payload)
readable = beautify_bytes_dict(decoded)

print("\n===== RTPengine Active Call List =====")
print(json.dumps(readable, indent=4, ensure_ascii=False))


for call_id in decoded[b'calls']:
    print(call_id)

    # 準備 query 命令
    cookie = b"1_2393_6"
    query_payload = bencodepy.encode({
        b'command': b'query',
        b'call-id': call_id  # 已經是 bytes
    })
    query_message = cookie + b' ' + query_payload
    sock.sendto(query_message, server_address)

    data, server = sock.recvfrom(8192)
    cookie, payload = data.split(b" ", 1)
    bencoded_data = bencodepy.decode(payload)
    readable_query = beautify_bytes_dict(decoded_query)

    print(json.dumps(readable_query, indent=4, ensure_ascii=False))

sock.close()

