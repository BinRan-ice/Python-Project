# coding:utf-8
def happy_birthday(name,age):
    print('祝{0}生日快乐'.format(name))
    #print('祝'+name+'生日快乐')  can only concatenate str (not "int") to str
    print(str(age)+'岁生日快乐')

#函数调用
#happy_birthday('努尔夏提')  TypeError: happy_birthday() missing 1 required positional argument: 'age'
happy_birthday(18,'努尔夏提')   #程序不报错语义不对

#正确的传递方式
happy_birthday('努尔夏提',18)
