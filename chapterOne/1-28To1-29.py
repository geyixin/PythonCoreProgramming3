import re

# 1-28 #

# s = '(\d{3}-)?(\d{3})-(\d{4})'
# m = re.search(s, '555-1212')
# print(m.group())

# 1-29 #

s = '((\d{3}-)|(\(\d{3}\) ))?(\d{3})-(\d{4})'
m = re.search(s, '(800) 555-1212')
print(m.group())