#!usr/bin/env python
# -*- coding: utf-8 -*-

# 使用SMTP 和POP3 创建一个既能接收和下载电子邮件也能上传和发送电子邮件的客户端

from smtplib import SMTP
from poplib import POP3

SMTPSVR = 'smtp.python.is.cool'
POP3SVR = 'pop.python.is.cool'

who = 'cccccc@163.com'
body = '''\
From: %(who)s
To: %(who)s
Subject: test msg, haha
Hello World!
''' % {'who': who}

sendSVR = SMTP(SMTPSVR)
errs = sendSVR.sendmail(who, [who], msg='xin')
sendSVR.quit()
assert len(errs) == 0, errs
sleep(10)

recvSVR = POP3(POP3SVR)
recvSVR.user('xiaoming')
recvSVR.pass_('xxxxxxxxx')
rsp, msg, siz = recvSVR.retr(recvSVR.stat()[0])
sep = msg.index('')
recvBODY = msg[sep+1:]
assert origBODY == recvBODY













