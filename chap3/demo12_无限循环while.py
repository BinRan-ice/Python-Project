# coding:utf-8
#1.初始化变量
answer=input('今天上课么：y/n?')
while answer=='y':  #2.条件判断
    print('好好学习 天天向上')  #3.循环体
    #4.改变变量
    answer=input('今天上课么：y/n?')

#1-100之间的累加和
i=1
s=0
while i<=100:
   s+=i
   i+=1
print(s)