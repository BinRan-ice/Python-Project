# coding:utf-8
def happy_birthday(name='蔡徐坤',age=100):
    print('祝{0}生日快乐'.format(name))
    print(str(age)+'岁生日快乐')

#采用默认值调用
happy_birthday()
happy_birthday('努尔夏提')  #age使用了默认值
happy_birthday(age=19)  #使用了关键字传参，name使用默认值
happy_birthday(19)
#同时存在默认值参数，位置参数时，默认值参数放后面

def fun(a,b):
    pass

#def fun2(a=12,b):
#    pass