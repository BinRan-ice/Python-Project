# coding:utf-8
#个数可变的位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(item)

#调用时参数传递
fun(10,20,30,40)
fun(10)
fun(10,'hello',3.14)
print('*'*50)
fun([10,20,30,40,50])
#调用时参数前加一个星，会将列表进行解包
fun(*[10,20,30,40,50])

#个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'---',value)

#调用
fun2(name='努尔夏提',age=18,height=170)
d={'name':'努尔夏提','age':18,'height':170}
#fun2(d) TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d)