# coding:utf-8
x=10
y=3
z=x/y   #在执行除法运算，赋值给z
print(z,type(z))    #隐式转换，通过运算隐式转换结果的数据

#将float类型转换成int类型,只保留整数部分
print('float类型转换成int类型',int(3.14))
print('float类型转换成int类型',int(3.9))
print('float类型转换成int类型',int(-3.9))
print('float类型转换成int类型',int(-3.14))

#将int类型转换成float类型
print('将int类型转换成float类型',float(10))

#将str类型转换成int类型
print(int('200')+int('100'))

#将str类型转换成float类型
print('#将str类型转换成float类型',float("3.14"))

#将str类型转换成int或float类型报错的情况
#print(int('18a'))    invalid literal for int() with base 10: '18a'
#print(int('3.14'))   invalid literal for int() with base 10: '3.14'
#print(float('54.12q'))  could not convert string to float: '54.12q'

#chr()与ord()函数
print(ord('杨')) #26472  将字符‘杨’转成对应的整数值
print(chr(26472))   #将整数值转成对应的字符

#进制之间的转换操作 十进制与其他进制之间的转换
print('十进制转成十六进制:'+hex(123))
print('十进制转成八进制：'+oct(123))
print('十进制转成十六进制：'+bin(123))
