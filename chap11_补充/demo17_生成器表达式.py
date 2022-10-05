# coding:utf-8
g=(i for i in range(5))
print(g)        #由于元组是不可变数据类型，所以g是一个生成器对象
"""
拿空生成器的数据：
        1.直接for循环
        生成器->迭代器->可迭代对象->for循环
        for item in g:
            print(item)
        2.可以使用list，tuple，set直接把生成器拿空
        print(list(g))
"""

def func():     #生成器函数
    print(111)
    yield 222


g=func()        #创建生成器
g1=(i for i in g)       #g1也是一个生成器
g2=(i for i in g1)      #g2也是生成器

print(list(g))      #这里直接把g拿空，此时g1没数据，g2没数据
print(list(g1))
print(list(g2))

def func1():
    lst1=["麻花1","沈腾1","玛丽1"]
    lst2=["麻花2","沈腾2","玛丽2"]
    """
    方法和下面一样：
        for item in lst1:
            yield item
        for item in lst2:
            yield item
    """
    yield from lst1     #把一个可迭代对象中的每一项分别返回
    yield from lst2

g=func1()
print(list(g))