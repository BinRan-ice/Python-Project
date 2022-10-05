# coding:utf-8
lst=["张无忌","谢广坤","张程程"]
#for循环内部大致的工作机制
it=lst.__iter__()       #拿到迭代器
while True:
    try:        #尝试执行下面的代码
        obj=it.__next__()       #拿到数据
        print(obj)
    except StopIteration:       #如果上方代码出现了StopIteration这样的错误，这段代码就开始执行
        break