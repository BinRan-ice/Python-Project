# coding:utf-8
def happy_birthday(name,age):
    print('祝{0}生日快乐'.format(name))
    print(str(age)+'岁生日快乐')

happy_birthday('陈美美',18)
#关键字传参
happy_birthday(age=18,name='陈美美')
happy_birthday(name='陈美美',age=18)   #参数的名称必须与函数定义的参数名称相同
happy_birthday('韩梅梅',age=18)    #第一个参数使用位置参数传参，第二个参数使用关键字参数传参
#happy_birthday(name='韩梅梅',18)   #SyntaxError: positional argument follows keyword argument
#位置参数在关键字参数之后就会报错