# coding:utf-8
s='3.14+3'
print(s,type(s))
x=eval(s)   #执行了加法运算
print(x,type(x))

#eval()函数经常和input()函数一起使用，用来获取用户输入的数值型
age=eval(input('请输入你的年龄：')) #将字符串类型转换成int类型，相当于int(age)
print(age,type(age))

height=eval(input('请输入您的身高：'))
print(height,type(height))

#使用eval报错的情况
print(eval('hello'))    #name 'hello' is not defined. Did you mean: 'help'?