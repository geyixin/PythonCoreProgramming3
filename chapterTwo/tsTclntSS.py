#uer/bin/env python
# -*- coding: utf-8 -*-
# socketserver 时间戳TCP 客户端

from socket import *

HOST = 'localhost'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 每次向服务器发送消息时，都需要创建一个新的套接字。
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(b"%s\r\n" % data.encode())
    # tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data.strip())
    tcpCliSock.close()
