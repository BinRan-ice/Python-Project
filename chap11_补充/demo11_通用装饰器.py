# coding:utf-8
#通用装饰器的写法
def wrapper(fn):
    def inner(*args,**kwargs):      #任意的参数都能接受
        """在执行目标函数之前"""
        ret=fn(*args,**kwargs)      #这里才是真正的目标函数
        """在执行目标函数之后"""
        return ret
    return inner

#装饰器的应用
#写装饰器，在执行目标函数的时候，判断是否登录
#如果没有登录，请登录，确保用户在登陆成功之后，再执行目标
flag=False      #默认没登录

def login_verify(fn):
    """
    这里是登录验证的装饰器
    :param fn: 被装饰的函数
    :return: ineer
    """
    def inner(*args,**kwargs):
        while 1:        #反复的判断登录状态
            if flag:
                ret=fn(*args,**kwargs)      #执行目标
                return ret      #返回结果
            else:
                login()
    return inner

def login():
    global flag
    username=input("请输入用户名：")
    password=input("请输入密码：")
    if username=="admin" and password=="123456":
        flag=True
        print("登陆成功")
    else:
        print("登陆失败")

@login_verify
def add():
    print("我要执行新增操作")

@login_verify
def upd():
    print("我要执行更新操作")

add()
upd()