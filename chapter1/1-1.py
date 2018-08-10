'''
# 正则表达式:
# 为高级的文本模式匹配、抽取、与/或文本形式的搜索和替换功能提供了基础。
# 简单地说，正则表达式（简称为regex）是一些由字符和特殊符号组成的字符串，它们描述了
# 模式的重复或者表述多个字符，于是正则表达式能按照某种模式匹配一系列有相似特征的字
# 符串（见图1-1）。换句话说，它们能够匹配多个字符串。
'''


import re

# match 与search的不同：

# m = re.match('foo', 'I like delicious food')  # 不在前面，无法匹配
# m1 = re.match('foo', 'food I like delicious')  # 只能匹配在最前面出现的
# m2 = re.search('foo', 'I like delicious food')  # 只要有，即可
# print(m, m1.group(), m2.group())  # 当输出为None(没有匹配成功)，则没有group等函数功能

# . 可以匹配出\n之外的任何字符

# anyend = '.end'
# m = re.match(anyend, 'pend')
# m1 = re.match(anyend, '\nend')
# print(m.group(), m1)

# patt314 = '3.14'  # 这个点号是正则表达式的点号
# pat = '3\.14'  # 表示数学中的点号
# m = re.match(patt314, '3014')
# m2 = re.match(patt314, '3.14')
# m3 = re.match(pat, '3014')  # 无法匹配
# m4 = re.match(pat, '3.14')
# print(m.group(), m2.group(), m3, m4.group())

# []  |  都是选择其一
# m = re.match('[as][56][fg]', 'a5f')
# m1 = re.match('[as][56][fg]', 'a6f')
# m2 = re.match('[as][56][fg]', 's5f')
# m3 = re.match('[as][56][fg]', 's6g')
# m4 = re.match('[as][56][fg]', 'as5')  # 无法匹配
# m5 = re.match('[as][56][fg]', '35f')  # 无法匹配
# m6 = re.match('a5f|s5f', 'a5f')  # 只能匹配 | 的前后存在的两个
# m7 = re.match('a5f|s5g', 'a5g')
# print(m.group(), m1.group(), m2.group(), m3.group(), m4, m5, m6.group(), m7)

# () 的使用：形成独立子组

# m = re.match('(\w\w\w)-(\d\d\d)', 'asd-123')  # 两个子组
# m1 = re.match('\w\w\w-(\d\d\d)', 'asd-123')  # 一个子组
# print(m.group())
# print(m.groups())
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m1.group())
# print(m1.groups())
# print(m1.group(0))
# print(m1.group(1))

# ^ 匹配字符串的开始， \b 边界匹配$ 匹配字符串的结尾

# m = re.search('^From', 'From xi to ming')
# m1 = re.search(r'\bfrom', 'from xi to ming')  # 注意两个 \b 颜色不同，前面加了r
# m2 = re.search('\bfrom', 'from xi to ming')
# m3 = re.search(r'\bfrom', 'learn from xi to ming')
# m4 = re.search(r'\Bfrom', 'learnfrom xi to ming')
# # m1 = re.search('^From', 'learn From xi to ming')  # From未作为开头，无法匹配
# print(m.group(), m1.group(), m2, m3.group(), m4.group())

# findall():查询字符串中某个正则表达式模式全部的非重复出现情况，与search()功能类似，但是
#  findall()返回的是列表。没有匹配到，返回空列表。
# finditer()与findall()功能类似，只是返回的是迭代器，注意看其如何输出匹配结果。
# 而且m1.__next__().groups()类型是tuple
# m = re.findall('car', 'carry the barcardi to the car')
# m1 = re.finditer('(th\w+) and (th\w+)', 'This and that', re.I)  # re.I:不区分大小写
# m2 = [g.groups() for g in re.finditer('(th\w+) and (th\w+)', 'This and that', re.I)]
# print(m)  # list
# print(m1.__next__().groups())  # tuple
# print(m2)  # list

# sub() 和 subn() 完成搜索和替换。subn()会返回替换的总数。

# m0 = re.sub('X', 'Mr.Smith', 'attn: X\n\nDear X, \n')
# m1 = re.subn('X', 'Mr.Smith', 'attn: X\n\nDear X, \n')
# m2 = re.subn('[ae]', 'X', 'asdfceare')
# print('m0:', m0)
# print('m1:', m1)
# print('m1[0]:', m1[0])
# print('m1[1]:', m1[1])
# print('m2:', m2)

# 使用sub() + \n 进行次序重排：r'\2/\1/\3'，这是新的次序。

# da = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91')
# da2 = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/1991')
# print(da)  # 20/2/91
# print(da2)

# re中的split，我个人感觉能有正常的split就不用re的split

# s1 = 'str1:str2:str3'
# s2 = re.split(':', s1)
# s3 = s1.split(':')
# print(s1, s2, s3, s2==s3)

# data = ('Mountain View, CA 94040', 'Sunnyvale, CA',
#         'Los Altos, 94023', 'Cupertino 95014', 'Palo Alto CA',)
# for datum in data:
#     print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))
# (?:\d{5}|[A-Z]{2})，表示以5个数字或者2个大写字母作为结尾
# ?= 表示后面跟的是=后面的东西才行

# 扩展字符串：?i，不区分大小写; ?im，多行不区分大小写; ?s，可以匹配\n;
#  ?x, 用户通过抑制在正则表达式中使用空白符（除了在字符类中或者在反斜线转义中）来创建更易读的正则表达式
# ?:, 对部分正则表达式进行分组，但是并不会保存该分组用于后续的检索或者应用
# print(re.findall('(?i)yes', 'yes,Yes,YES,YeS'))
# print(re.findall('(?im)(^th[\w ]+)', '''
# This line is the first
# another line
# that line, it\'s the best'''))
# print(re.findall('((?s)th.+)', '''
# This line is the first
# the other line
# that line, it\'s the best'''))
# m = re.search(r'(?x)\((\d{3})\)[ ](\d{3})-(\d{4})', '(800) 555-1212').groups()
# print(m)
# m = re.findall(r'http://(\w+\.)*(\w+\.com)', 'http://google.com'
#                                              'http://www.google.com'
#                                              'https://code.google.com')
# m1 = re.findall(r'(\w+\.)*(\w+\.com)', 'http://google.com'
#                                              'http://www.google.com'
#                                              'https://code.google.com')
# m2 = re.findall(r'http://(?:\w+\.)*(\w+\.com)', 'http://google.com'
#                                              'http://www.google.com'
#                                              'https://code.google.com')
# m3 = re.findall(r'(?:\w+\.)*(\w+\.com)', 'http://google.com'
#                                              'http://www.google.com'
#                                              'https://code.google.com')
# print(m)
# print(m1)
# print(m2)
# print(m3)

# ?P<name>, 实现字典风格的检索匹配结果
# ?P=name， 可以在一个相同的正则表达式中重用模式，而不必稍后再次在（相同）
# 正则表达式中指定相同的模

# m = re.search(r'\((?P<name1>\d{3})\) (?P<name3>\d{3})-(?:\d{4})', '(800) 555-1212').groupdict()
# print(m, m['name1'])
# m = re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) '
#              r'(?P=areacode)-(?P=prefix)-(?P=number) '
#              r'1(?P=areacode)(?P=prefix)(?P=number)',
#              '(800) 555-1212 800-555-1212 18005551212')
# print(m.group())

# 假定我们拥有另一个特殊字符，它仅包含字母“x”和“y”，
# 我们此时仅仅想要这样限定字符串：两字母的字符串必须由一个字母跟着另一个字母。
# 换句话说，你不能同时拥有两个相同的字母；要么由“x”跟着“y”，要么相反

# m = re.search(r'((x)|y)(?(1)y|x)', 'xy')
# m1 = re.search(r'((x)|y)(?(1)y|x)', 'yx')  # None
# m2 = re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')
# m3 = re.search(r'(?:(x)|y)(?(1)y|x)', 'yx')
# print('m', m.group())
# print('m1', m1)
# print('m2', m2.group())
# print('m3', m3.group())

# \s\s+, 切割两个及两个以上的空白符
# 前面加r，是为了避免转义特殊字符串\n等

# s = 'System Idle Process      0 Console       0      28 K'
# m = re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ k)', s)
# print(m)

# s = 'ssde.v ds e.r p,u ppp.www'
# m1 = re.findall(r'(\w+)', s)     # 只要没有连在一起，就切割
# m2 = re.findall(r'(\w.+)', s)    #
# m3 = re.findall(r'([\w]+)', s)   #
# m4 = re.findall(r'([\w.]+)', s)  # 切割所有没连在一起的，除了点：.。
# print(m1)
# print(m2)
# print(m3, m1==m3)
# print(m4)


# s = 'Sat Dec 24 22:10:53 1994::gfpn@pevbtjcv.com::788278253-4-8'
# r = '.+?(\d+-\d+-\d+)'
# r1 = '.+(\d+-\d+-\d+)'  # .+实现的是贪婪匹配，需要使用?，减少.+的匹配
# r2 = '(\d+-\d+-\d+)'
# m = re.search(r, s)
# m1 = re.search(r1, s)
# m2 = re.search(r2, s)
# m3 = re.split('::', s)[2].split('-')[1]
# print(m.group(1))
# print(m1.group(1))
# print(m2.group(1))
# print(m3)
# r3 = '-(\d+)-'
# m4 = re.search(r3, s)
# print(m4.group(1))









