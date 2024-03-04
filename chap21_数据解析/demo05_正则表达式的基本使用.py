# coding:utf-8
import re
s='I study study Python3.8 every day'
print("------------match方法，从起始位置开始匹配------------")
print(re.match('I',s).group())
print(re.match('\w',s).group())
print(re.match('.',s).group())
print("---------------search方法，从任意位置开始匹配，匹配第一个----------------")
print(re.search('study',s).groups())
print(re.search('s\w',s).group())
print("---------------findall方法，从任意位置开始匹配，匹配多个------------------")
print(re.findall('y',s))
print(re.findall('python',s))
print(re.findall('P\w+.\d',s))
print(re.findall('P.+\d',s))
print('-----------sub方法，替换功能------------')
print(re.sub('study','like',s))
print(re.sub('s\w+','like',s))