# coding:utf-8
x=True
print(x)
print(type(x))
print(True+10)  #1+10
print(False+10) #0+10

print('------------------')
#测试对象的布尔值
print(bool(18)) #True
print(bool(0),bool(0.0))    #False
#总结，非0的数值型布尔值都是True
print(bool('北京欢迎你'))    #True
print(bool('')) #空字符串的布尔值为False
print(bool(False))
print(bool(None))