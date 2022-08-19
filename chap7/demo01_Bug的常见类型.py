# coding:utf-8
age=input('请输入你的年龄：')
print(type(age))
if int(age)>=18:
    print('成年人。。。。')

i=0
while i<10:
    i+=1
    print(i)

lst=[11,22,33,44]
#print(lst[4])  索引越界

lst=[]
#lst=append('A','B','C')
lst.append('A')
lst.append('B')
lst.append('C')