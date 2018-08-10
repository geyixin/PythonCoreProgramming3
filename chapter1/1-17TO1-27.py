# -*- coding: utf-8 -*-

import re
import sys
import os
import time

# 执行语句：python 1-17TO1-27.py redata.txt

inputpath = sys.argv[1]
arr = []
if os.path.exists(inputpath):
    with open(inputpath, 'r') as ip:
        for line in ip:
            arr.append(line)
else:
    print('file not exist: ' + inputpath)

# 1-18、19、20、21、22、23、24、25 #

for hang in arr:
    data, email, jiaodui = hang.split('::')
    jiaoduiTime = jiaodui.split('-')
    # print(data == time.ctime(int(jiaoduiTime[0])))  # 1-18
    # print(data)  # 1-19
    # print(email)  # 1-20
    # print(data.split()[1])  # 1-21
    # print(data.split()[-1])  # 1-22
    # print(data.split()[3])  # 1-23
    # s = '(\w+)@(\w+).(\w+)'   # 接着三行对应1-24
    # m = re.search(s, email)
    # print(m.groups())  # groups()就是分开显示，group()就是整体显示
    # myemail = '123@qq.com'  # 接着三行对应1-26
    # m = re.sub('(\w+)@(\w+).(\w+)', myemail, hang)
    # print(m)
    # week, yue, hao, tim, nian = data.split()  # 接着2行对应1-27
    # print('%s, %s, %s' % (yue, hao, nian))


