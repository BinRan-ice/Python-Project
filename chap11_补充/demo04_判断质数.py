# coding:utf-8
#练习：让用户随便输入一个数字，判断这个数字，是否是质数
n=int(input("请输入一个数字：").strip())
i=2
while i<n:
    if n%i==0:
        print("不是质数")
        break
    i+=1
else:
    print("是质数")