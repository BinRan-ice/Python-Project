# coding:utf-8
def wrapper1(fn):
    def inner(*args,**kwargs):
        print("wrapper1-before")
        ret=fn(*args,**kwargs)
        print("wrapper1-after")
        return ret
    return inner

def wrapper2(fn):
    def inner(*args,**kwargs):
        print("wrapper2-before")
        ret=fn(*args,**kwargs)
        print("wrapper2-after")
        return ret
    return inner

def wrapper3(fn):
    def inner(*args,**kwargs):
        print("wrapper3-before")
        ret=fn(*args,**kwargs)
        print("wrapper3-after")
        return ret
    return inner

@wrapper3
@wrapper2
@wrapper1
def target():       #按照就近原则去解读
    print("我是target")

target()