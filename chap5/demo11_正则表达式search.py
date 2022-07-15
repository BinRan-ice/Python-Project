# coding:utf-8
import re
pattern=r'\d\.\d+'
s='I study Python3.10 every day Python2.10 I love you'
s2='4.10Python I study every day'
s3='I study Python every day'
print(re.search(pattern,s))
print(re.search(pattern,s2))
print(re.search(pattern,s3))

