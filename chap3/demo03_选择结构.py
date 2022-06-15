# coding:utf-8
number=eval(input('请输入您的六位中奖号码：'))
#使用if语句
if number==987654:
    print('恭喜您，中奖了')

if number !=987654:
    print('您未中本期大奖')
print('----------以上if判断的表达式，使用比较运算符,比较表达式------------')

n=97    #赋值
if n%2: #98%2的余数为0,0的布尔值为False，非0的布尔值为True
    print(n,'为奇数')

if not n%2: #98%2的余数为0，0的布尔值为False，not False的布尔值为True
    print(n,'n为偶数')

print('--------------判断空字符串----------------')
x=input('请输入一个字符串：')    #空字符串的布尔值为False，非空字符串的布尔值为True
if x:
    print('x是一个非空字符串')

if not x:
    print('x是一个1空字符串')

print('-------------表达式也可以是一个变量---------------')
flag=eval(input('请输入一个布尔类型的值：True OR False'))
if flag:
    print('flag的值为True')

if not flag:
    print('flag的值为False')

print('----------使用if语句时，如果语句块只有一句代码，可以将语句块直接写在：的后面------------')
a=10
b=5
if a>b:max=a
print('a和b的最大值为：',max)