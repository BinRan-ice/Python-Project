# coding:utf-8
#直接使用()创建元组
t=('hello',[10,20,30],'python','world',[10,'world'])
print(t)

#使用内置函数tuple()创建元组
t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

t=tuple(range(1,10))
print(t)

#元组的相关操作
print('10在元组中是否存在:',(10 in t))
print('10在元组中不存在:',(10 not in t))
print('求最大值：',max(t))
print('求最小值：',min(t))
print('求长度:',len(t))
print('t.index:',t.index(1))
print('t.count:',t.count(4))

x=(10)
print(type(x))  #int类型

y=(10,)
print(type(y))  #tuple元组类型

#元组的删除
del t
print(t)