# coding:utf-8
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0}，今年{1}岁了'.format(self.name,self.age)


stu=Student('张三',20)
print(dir(stu))
print(stu)#默认调用__str__()方法
print(type(stu))