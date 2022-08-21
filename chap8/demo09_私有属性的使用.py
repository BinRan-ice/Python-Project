# coding:utf-8
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希望在类的外部使用，加__
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
#在类的外部使用name和age
print(stu.name)
#print(stu.__age)    #AttributeError: 'Student' object has no attribute '__age'
print(dir(stu))
print(stu._Student__age)    #在类的外部可以通过_Student__age进行访问