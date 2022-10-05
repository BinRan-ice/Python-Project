# coding:utf-8
def gua_outer(name):
    def gua(fn):
        def inner(*args,**kwargs):
            print(f"开启{name}外挂")
            ret=fn(*args,**kwargs)
            print("关闭外挂")
            return ret
        return inner
    return gua

@gua_outer("饕餮")        #先执行函数的调用，函数返回一个装饰器，和@组合成语法糖，@gua
def dnf():
    print("我要打卢克")

@gua_outer("耄耋")
def lol():
    print("我要杀遍全场")

dnf()
lol()