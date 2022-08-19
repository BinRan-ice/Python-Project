# coding:utf-8

try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数:'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为0！！！')
except ValueError:
    print('有非数字字符出现！！！')
except BaseException as e:
    print(e)