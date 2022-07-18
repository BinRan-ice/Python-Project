# coding:utf-8
import re
pattern='黑客|破解|反爬'
s='我想学习python，想破解一些vip视频，Python可以实现无底线反爬么？'
new_s=re.sub(pattern,'XXX',s) #字符串的替换
print(new_s)

s2='https://www.baidu.com/s?wd=next&ie=utf-8&tn=baidu'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)