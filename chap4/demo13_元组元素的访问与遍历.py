# coding:utf-8
t=('python','hello','world')
print(t[0]) #根据索引访问
t2=t[0:3:2] #元组支持切片操作
print(t2)
#元组的遍历
for item in t:
    print(item)

#for+range()+len()组合遍历
for i in range(len(t)):
    print(i,t[i])

#使用enumerate()
for index,item in enumerate(t,0):
    print(index,'-->',item)

