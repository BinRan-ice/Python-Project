# coding:utf-8
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',18)
stu2=Student('李四',30)
print('***********为stu2动态绑定性别属性************')
stu2.gender='女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

print('----------------------------')
stu1.eat()
stu2.eat()

def show():
    print('定义在类之外的函数')
stu1.show=show  #动态绑定show方法
stu1.show()
#stu2.show() AttributeError: 'Student' object has no attribute 'show'