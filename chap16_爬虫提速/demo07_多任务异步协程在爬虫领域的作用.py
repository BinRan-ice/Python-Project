# coding:utf-8
import asyncio

async def download(url):
    print("准备下载")
    await asyncio.sleep(2)  #网络请求
    print("下载完成")

async def main():
    urls=[
        "http://www.baidu.com",
        "http://www.163.com",
        "http://www.bilibili.com"
    ]
    tasks=[]
    for item in urls:
        d=download(item)
        tasks.append(asyncio.create_task(d))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())