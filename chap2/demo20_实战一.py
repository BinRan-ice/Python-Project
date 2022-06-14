# coding:utf-8
num=eval(input('请输入一个四位整数：'))
a=num//1000
b=num//100%10
c=num//10%100%10
d=num%1000%100%10
print('个位数：',d)
print('十位数：',c)
print('百位数：',b)
print('千位数：',a)