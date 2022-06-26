# coding:utf-8
t=(i for i in range(1,11))  #结果是一个生成器对象
print(t)
#t=tuple(t)
#print(t)

#for item in t:
#    print(item)

#__next__()方法
print(t.__next__())
print(t.__next__())
print(t.__next__())

#t=tuple(t)
#print(t)
print('-----------------------')
for item in t:
    print(item)
