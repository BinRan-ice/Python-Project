# coding:utf-8
#(1)直接使用{}创建
d={10:'cat',20:'dog',30:'pet',20:'zoo'} #key相同，值进行覆盖
print(d)

#(2)zip()函数的使用
lst1=[10,20,30,40]
lst2=['cat','dog','car','zoo']
zipobj=zip(lst1,lst2)   #映射函数的结果是一个zip对象
#print(zipobj)
#for item in zipobj:
#    print(item)
d=dict(zipobj)
print(d)

#(3)使用参数创建字典
d=dict(cat=10,dog=20)   #注意事项，参数相当于变量，名字不需要加引号
print(d)

t=(1,20,30) #创建一个元组
print({t:10})

#lst=[10,20,30]  TypeError: unhashable type: 'list'
#print({lst:23})    列表是可变数据类型，不能做key值

#字典属于序列类型
print('max',max(d))
print('min',min(d))
print('len',len(d))

#字典的删除
del d
print(d)    #NameError: name 'd' is not defined. Did you mean: 'id'?