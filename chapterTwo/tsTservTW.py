#!usr/bin/env python
# -*- coding: utf-8 -*-
# Twisted Reactor 时间戳TCP 服务器

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    # 当一个客户端连接到服务器时就会执行connectionMade()
    def connectionMade(self):  # 重写connectionMade()
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt)
    # 当服务器接收到客户端通过网络发送的一些数据时就会调用dataReceived()
    def dataReceived(self, data):  # 重写dataReceived()
        self.transport.write(('[%s] %s' % (ctime(), data)).encode())

factory = protocol.Factory()  # 协议工厂
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()