# coding:utf-8
#程序是可以自己抛出异常的
def func(a,b):  #计算两个int类型的数字的和
    if type(a)==int and type(b)==int:
        return a+b
    else:
        #抛出异常，谁调用该函数，谁接收该异常
        raise Exception("你给我的不是int类型，func函数无法进行计算")

func("呵呵",1)

"""
1.处理异常  try...except
2.抛出异常  raise
"""