# coding:utf-8
import requests


url="https://new.qqaku.com/20220927/eJaR8Ckw/1100kb/hls/playlist_up.m3u8"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp=requests.get(url,headers=headers)
with open("videos/唐朝诡事录.m3u8",mode="wb") as f:
    f.write(resp.content)
resp.close()


#解析m3u8文件
n=1
with open("videos/唐朝诡事录.m3u8",mode="r",encoding="utf-8") as f:
    for line in f:
        line=line.strip()       #去掉空格，空白，换行符
        if line.startswith("#"): #如果以#开头，不要
            continue
        #下载视频的片段
        resp2=requests.get(line)
        f=open(f"videos/{n}.ts",mode="wb")
        f.write(resp2.content)
        f.close()
        resp2.close()
        n+=1
        print(f"完成了{n-1}个")
