# coding:utf-8
#装饰器：可以在不改变原来的代码基础上，给函数添加新的功能
#可以在原有操作前面或者后面随意的添加新的功能
def wrapper1(fn):        #把被装饰的函数传递进来
    def inner():
        print("这里是被装饰函数执行之前")
        fn()        #执行被装饰的函数
        print("被装饰函数执行之后")
    return inner        #把内层函数返回

def add1():
    print("我是新增函数")

#a=wrapper1(add1)      #a就是inner
#a()     #执行的是inner

#add1=wrapper1(add1)        #此时的add就变成了inner
#add1()       #此时执行的是inner函数


#语法糖
def wrapper(fn):
    def inner():
        print("在执行目标函数之前")
        fn()
        print("在执行目标函数之后")
    return inner

@wrapper
def add():
    print("我叫add")

# add=wrapper(add)  #这句话可以被替代成@wrapper
add()

#在不改变原来函数的基础上，给函数添加新的功能