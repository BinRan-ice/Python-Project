# coding:utf-8
#赋值运算符的执行顺序：从右到左
name='努尔夏提' #将努尔夏提赋值给变量name
age=20  #将20赋值给变量age

a=b=c=d=100 #将a,b,c,d的值同时赋值为100，链式赋值
#系列解包赋值
name1,age1='李四',22  #元组分解赋值
print(name1,age1)
[name2,age2]=['王五',22]  #列表分解赋值
print(name2,age2)

a,b,c,d='room'  #字符串分解赋值
print(a)
print(b)
print(c)
print(d)

#拓展的字符串解包赋值
a,*b='room'
print(a,b)

print('----------输入输出语句,也是典型的顺序结构------------')
name=input('请输入您的姓名：')
age=eval(input('请输入您的年龄：'))
luck_number=eval(input('请输入您的幸运数字：'))
print('姓名：',name)
print('年龄：',age)
print('幸运数字:',luck_number)


