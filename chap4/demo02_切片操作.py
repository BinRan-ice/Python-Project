# coding:utf-8
s='HelloWorld'
s1=s[0:5:1] #索引从0开始到5结束，不包括5，步长为1
print(s1)
#省略开始位置start
print(s[:5:1])
#既省略开始位置start，又省略步长step
print(s[:5])
#省略结束位置
print(s[0::1])
#省略结束位置和步长
print(s[5:])
#更换步长
print(s[0:5:2])
#省略开始位置和结束位置，只写步长
print(s[::2])
#步长可以为负数
print(s[::-1])