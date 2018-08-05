#!usr/bin/env python
# -*- coding: utf-8 -*-
# 创建UDP 客户端
from socket import *

HOST = 'localhost'
PORT = 21570
BUFSIZ = 1024
ADDR = (HOST, PORT)
udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode(), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    data = data.decode()
    print('data=', data)
    if not data:
        break
    print(data)
udpCliSock.close()


