# coding:utf-8
#直接使用[]创建
lst=['hello','world',99.8,100]
print(lst)
for i in range(0,len(lst)):
    print(lst[i])

#可以使用内置函数list()创建列表
lst2=list('helloworld')
lst3=list(range(1,10,2))
print(lst2)
print(lst3)

#列表是序列中的一种，对序列操作的运算符，操作符，函数均可以使用
print(lst+lst2+lst3)    #序列中相加的操作
print(lst*3)    #序列中相乘的操作
print(len(lst))
print(max(lst3))
print(min(lst2))
print(lst3.count(1))    #统计1的个数
print(lst2.index('d'))  #统计‘d’在lst2中首次出现的位置

#列表中的删除操作
lst4=[20,30,40]
print(lst4)
#删除列表
del lst4
#print(lst4) NameError: name 'lst4' is not defined. Did you mean: 'lst'?