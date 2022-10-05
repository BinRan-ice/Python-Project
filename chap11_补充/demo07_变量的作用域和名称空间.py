# coding:utf-8
a = 10
def haha():
    pass
#全局作用域内容：全局名称空间+内置名称空间
print(globals())    #globals可以查看全局作用域中的内容

def func():
    a = 10
    def hehe():
        pass
    print(locals())     #查看当前作用域中的内容
func()


print(locals())     #查看当前作用域
print(globals())    #查看全局作用域