# coding:utf-8
x=20    #直接赋值，直接将20赋值给左侧的变量x
y=10
x=x+y   #将x+y的和赋值给x,x的值为30
print(x)
x+=y
print(x)    #40
x-=y
print(x)    #30
x*=y
print(x)    #300
x/=y
print(x)    #30
x%=2
print(x)    #0.0
z=3
y//=z
print(y)    #3

y**=2
print(y)    #9

#python支持链式赋值
a=b=c=100
print(a,b,c)

#Python支持系列解包赋值
a,b=10,20
print(a,b)

print('--------如何交换两个变量的值---------')
a,b=b,a
print(a,b)
