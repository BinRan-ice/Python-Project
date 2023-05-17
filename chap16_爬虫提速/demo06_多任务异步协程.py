# coding:utf-8
#python编写协程程序
import asyncio
import time

"""
async def func():
    print("你好啊,我叫赛利亚")

if __name__ == '__main__':
    g=func()  #此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
    asyncio.run(g)      #协程程序运行需要asyncio模块的支持
"""

"""
async def func1():
    print("你好啊,我叫赛利亚")
    #time.sleep(3)       #当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(3)    #异步操作的代码
    print("你好啊，我叫赛利亚")

async def func2():
    print("你好啊,我叫王建国")
    #time.sleep(2)
    await asyncio.sleep(2)
    print("你好啊，我叫王建国")

async def func3():
    print("你好啊,我叫李雪琪")
    #time.sleep(4)
    await asyncio.sleep(4)
    print("你好啊，我叫李雪琪")

if __name__ == '__main__':
    f1=func1()
    f2=func2()
    f3=func3()
    tasks=[
        f1,f2,f3
    ]
    #一次性启动多个任务（协程）
    t1=time.time()
    asyncio.run(asyncio.wait(tasks))
    t2=time.time()
    print(t2-t1)
"""

async def func1():
    print("你好啊,我叫赛利亚")
    await asyncio.sleep(3)
    print("你好啊，我叫赛利亚")

async def func2():
    print("你好啊,我叫王建国")
    await asyncio.sleep(2)
    print("你好啊，我叫王建国")

async def func3():
    print("你好啊,我叫李雪琪")
    await asyncio.sleep(4)
    print("你好啊，我叫李雪琪")

async def main():
    #第一种写法
    #f1=fun1()
    #await f1   一般await挂起操作放在协程对象前面

    #第二种写法（推荐）
    tasks=[
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())