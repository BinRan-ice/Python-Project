# coding:utf-8
import asyncio
import aiohttp

"""
requests.get() 同步的代码->异步操作aiohttp
"""

urls={
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220927/pl3hwe4tywp.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220927/2df13w1wue3.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220927/rcsoupjx2ww.jpg"
}

"""
#发送请求
#得到图片内容
#保存到文件
"""

async def aiodownload(url):
    name=url.split("/")[-1]
    # 发送请求
    #s=aiohttp.ClientSession() <--->    相当于requests
    async with aiohttp.ClientSession() as session:      #requests
        async with session.get(url) as resp:            #resp=requests.get()
            #请求回来，写入文件
            #resp.content.read() #等价于resp.content
            with open(f"images/{name}",mode="wb") as f:     #创建文件
                f.write(await resp.content.read())      #读取内容是异步的，需要await挂起
    print(name,"搞定")

async def main():
    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())