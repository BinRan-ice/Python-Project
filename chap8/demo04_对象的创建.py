# coding:utf-8
class Student:  #Student为类的名称，有一个或多个单词组成，每个单词的首字母大写，其余小写
    native_pace='吉林'    #直接写在类里面的变量-->类属性
    def __init__(self,name,age):
        self.name=name  #self.name称为实例属性，进行了一个赋值的操作
        self.age=age

    # 实例方法
    def eat(self):
        print('学生在吃饭')

    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')


#创建Student类的对象
stu1=Student('张三',20)
stu1.eat()  #对象名.方法名
print(stu1.name)
print(stu1.age)
print('*'*50)
Student.eat(stu1)   #与25行代码相同     类名.方法名（类对象）
