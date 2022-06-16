# coding:utf-8
#遍历字符串
for i in 'hello':
    print(i)

#range()函数，产生一个[N,M)的整数序列，包含N，不包含M
for i in range(1,11):
    #print(i)
    if i%2==0 :
        print(i)

#计算1-10之间的累加和
s=0 #用于存储累加和
for i in range(1,11):
    s+=i
print('1-10之间的累加和为：',s)

print('-------------计算水仙花数---------------')
for i in range(100,1000):
    a=i//100
    b=i//10%10
    c=i%10
    if i==(a**3+b**3+c**3):
        print(i)