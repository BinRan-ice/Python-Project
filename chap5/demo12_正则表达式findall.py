# coding:utf-8
import re
pattern=r'\d\.\d+'
s='I study Python3.10 every day Python2.10 I love you'
s2='4.10Python I study every day'
s3='I study Python every day'

lst=re.findall(pattern,s)
lst2=re.findall(pattern,s2)
lst3=re.findall(pattern,s3)
print(lst)
print(lst2)
print(lst3)