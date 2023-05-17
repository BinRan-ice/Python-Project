# coding:utf-8
import requests
import aiohttp
import aiofiles
import asyncio
import json

"""
https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"} ==>所有章节的内容（名称，id）
章节内部的内容：
https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}
"""

"""
1.同步操作：访问getCatalog，拿到所有章节的cid和名称
2.异步操作：访问getChapterContent,下载所有的文章内容
"""

async def aiodownload(cid,b_id,title):
    data={
        "book_id":b_id,
        "cid":f"{b_id}|{cid}",
        "need_bookinfo":1
    }
    data=json.dumps(data)
    url=f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic=await resp.json()
            async with aiofiles.open(f"e_books/西游记/{title}",mode="w",encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])  #把小说内容写入

async def getCatalog(url):
    resp=requests.get(url)
    lst=list(resp.json()["data"]["novel"]["items"])
    tasks=[]
    for item in lst:
        title=item['title']
        cid=item['cid']
        #准备异步任务
        tasks.append(asyncio.create_task(aiodownload(cid,b_id,title)))
    await asyncio.wait(tasks)
    resp.close()

if __name__ == '__main__':
    b_id="4306063500"
    url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'
    loop=asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(getCatalog(url))