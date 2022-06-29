# coding:utf-8
d={1001:'李梅',1002:'王华',1003:'张锋'}
print(d)
#向字典添加数据
d[1004]='张丽丽'   #直接使用赋值运算符=向字典添加元素
print(d)

#获取字典中所有的key
keys=d.keys()   #d.keys()结果是dict_keys,Python中的一种内部数据类型，专用于表示字典的key
#如果希望更好的显示数据，可以使用list或者tuple转成相应的数据类型
print(keys)
print(list(keys))
print(tuple(keys))

#获取字典中所有的values
values=d.values()
print(values)   #dict.values
print(list(values))
print(tuple(values))

#字典遍历时用到的一个方法items
items=d.items()
print(items)    #dict.items
print(list(items))
print(tuple(items))

print('------------------')

lst=list(items) #将字典中的数据转换成key-->values,以元组的方式进行展示
print(lst)
t=tuple(items)
print(t)
#直接使用dict()函数转换成字典
d=dict(lst)
d=dict(t)
print(d)

#使用pop函数
print(d.pop(1001))  #先获取键值对，再删除
print(d)
print(d.pop(1008,'不存在'))    #如果key不存在，结果就输出默认值‘不存在’

#随机删除
print(d.popitem())  #先获取键值对，再删除
print(d)

#清空字典中所有元素
d.clear()
print(d)

#python中一切皆对象，每一个对象都有一个布尔值
print(bool(d))