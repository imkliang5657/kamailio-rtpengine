import socket
import bencodepy
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

# 建立 UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('114.35.197.224', 12223)

# 初始 list 指令
cookie = b"0_2393_6"
payload = bencodepy.encode({b'command': b'list'})
message = cookie + b' ' + payload

# 傳送 list 指令
sock.sendto(message, server_address)
print('waiting to receive...')
data, server = sock.recvfrom(4096)

# 拆解回傳
cookie, payload = data.split(b' ', 1)
decoded = bencodepy.decode(payload)
readable = beautify_bytes_dict(decoded)

print("\n===== RTPengine Active Call List =====")
print(json.dumps(readable, indent=4, ensure_ascii=False))

# 針對每個 call-id 做 query
for call_id in decoded[b'calls']:
    print("\n🔍 Querying call-id:", call_id.decode())
    
    cookie = b"1_2393_6"
    query_payload = bencodepy.encode({
        b'command': b'query',
        b'call-id': call_id
    })
    query_message = cookie + b' ' + query_payload
    sock.sendto(query_message, server_address)

    data, server = sock.recvfrom(8192)
    _, payload = data.split(b' ', 1)
    decoded_query = bencodepy.decode(payload)
    readable_query = beautify_bytes_dict(decoded_query)

    print(json.dumps(readable_query, indent=4, ensure_ascii=False))

sock.close()

