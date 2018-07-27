import re

# 1-1  #

# s = '([b|h][a|i|u]t)'
# p = 'hit hut'
# m = re.findall(s, p)  # findall的结果是list类型
# print(m)

# 1-2  #

# s = '(\w+ \w+)'
# p = 'xiao ming'
# m = re.search(s, p)  # search 的结果需要group()或者groups()
# print(m.group())

# 1-3  #

# s = '(\w+, \w+)'
# p = 'xiao, ming'
# m = re.search(s, p)  # search 的结果需要group()或者groups()
# print(m.group())

# 1-4  # python标识符：字母(区分大小写）、_、数字（不能作为开头）

# s = '^([A-Z]|[a-z]|-)+'
# p = 'xiaoming'
# m = re.match(s, p)  # search 的结果需要group()或者groups()
# m2 = re.search(s, p)
# print(m.group())
# print(m2.group())

# 1-5 #  街道匹配

# s = '^(\d)+ \w+( \w+)?'
# # p = '1180 Bordeaux dsf'
# p = '1180 Bordeaux'
# m = re.match(s, p)
# print(m.group())

# 1-6 #  域名匹配

# s = '^(www).(\w+\.)*(\w+).(com|edu)$'
# p = 'www.yahoo.com'
# m = re.match(s, p)
# print(m.group())

# 1-6 #  电子邮件匹配

# s = '\w+@\w+.com'
# p = 'gp12ip@qq.com'
# m = re.match(s, p)
# print(m)

