# coding:utf-8

#print(dir(object))
class A:
    pass

class B:
    pass

class C(A,B):
    def __init__(self,name):
        self.name=name

#创建C类对象
x=C('Jack')     #x是c类型的一个实例对象
print(x.__dict__)   #查看实例对象属性的字典
print(C.__dict__)   #查看类对象属性，方法的字典
print('--------------')
print(x.__class__)  #输出对象所属于的类型
print(C.__base__)   #输出C类的最近的父类
print(C.__bases__)  #输出C类的父类的元组
print(C.__mro__)    #类的层次结构
print(A.__subclasses__())   #输出A类的子类的列表