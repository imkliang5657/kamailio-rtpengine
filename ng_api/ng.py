#Quick Python library for interfacing with Sipwise's fantastic rtpengine - https://github.com/sipwise/rtpengine
#Bencode library from https://pypi.org/project/bencode.py/ (Had to download files from webpage (PIP was out of date))

import bencode
import socket
import sys
import random
import string

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('114.35.197.224', 12223)     #Your server address

cookie = "0_2393_6"
data = bencode.encode({'command':'list'})

message = str(cookie) + ' ' + str(data)
print(message)


sent = sock.sendto(message.encode('utf-8'), server_address)

print('waiting to receive')
data, server = sock.recvfrom(4096)
print('received "%s"' % data)
data = data.split(" ", 1)       #Only split on first space
print("Cookie is: " + str(data[0]))
print("Data is: " + str(bencode.decode(data[1])))
print("There are " + str(len(bencode.decode(data[1])['calls'])) + " calls up on RTPengine at " + str(server_address[0]))
for calls in bencode.decode(data[1])['calls']:
    print(calls)
    cookie = "1_2393_6"
    data = bencode.encode({'command': 'query', 'call-id': str(calls)})
    message = str(cookie).encode('utf-8') + " ".encode('utf-8') + str(data).encode('utf-8')
    sent = sock.sendto(message, server_address)
    print('\n\nwaiting to receive')
    data, server = sock.recvfrom(8192)

    data = data.split(" ", 1)       #Only split on first space
    bencoded_data = bencode.decode(data[1])

    for keys in bencoded_data:
        print(keys)
        print("\t" + str(bencoded_data[keys]))

sock.close()
