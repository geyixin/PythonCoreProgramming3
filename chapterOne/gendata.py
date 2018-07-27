#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 课后习题1-16  #
# 用于正则表达式练习的数据生成器
from random import randrange, choice
from string import ascii_lowercase as lc
# ascii_letters ascii_lowercase ascii_uppercase 依次对应52个大小写，26个小写，26个大写字母
import time
import sys

pa = sys.argv[1]

tlds = ('com', 'edu', 'net', 'org', 'gov')

oup = []
for i in range(randrange(5, 11)):
    maxInt = int(time.time())  # 获取本地时间，以秒呈现，是小数，需取整
    dtint = randrange(maxInt)  # 随机产生0-maxInt（包括0，不包括maxInt）的整数
    dtstr = time.ctime(dtint)  # 把秒数变成时间，格式：星期 月 号 时:分:秒 年
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    # rand.choice(s),从字符串s中随机选一个。这个join要会用。这种for循环在一句话中使用的方法要注意。
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    temp = ('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))
    oup.append(temp)

    print(temp)

with open(pa, 'w') as outfile:
    for item in oup:
        outfile.write("%s\n" % item)


# login = ''.join(choice(lc) for j in range(llen))
# 上面这一行等价于下面这三行
# kk = ''
# for i in range(llen):
#     kk += ''.join(choice(lc))

# 执行代码：
# python gendata.py radata.txt