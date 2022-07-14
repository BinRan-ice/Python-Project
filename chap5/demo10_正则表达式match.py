# coding:utf-8
#导入
import re
pattern=r'\d\.\d+'
s='I study Python3.10 every day'
match=re.match(pattern,s,re.I)
print(match)

s2='3.10Python I study every day'
match2=re.match(pattern,s2,re.I)
print(match2)
print('匹配值的起始位置：',match2.start())
print('匹配的结束位置：',match2.end())
print('匹配区间的位置：',match2.span())
print('待匹配的字符串：',match2.string)
print('匹配的数据：',match2.group())