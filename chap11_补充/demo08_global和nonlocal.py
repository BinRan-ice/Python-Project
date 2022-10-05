# coding:utf-8
a = 10
def func():
    global a        #当前func函数内部使用的a都是全局的
    a=a+1
    print(a)
func()

def func1():
    a=10
    def func2():
        nonlocal a      #必须在局部，把外层中的xxx变量引入进来
        a+=1
        print(a)
    func2()
func1()

#只要出现了，在局部中使用外层变量，就需要使用global或者nonlocal