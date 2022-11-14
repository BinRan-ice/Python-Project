# coding:utf-8
import requests

"""
1.拿到contID
2.拿到video_status返回的json -> srcurl
3.srcurl里面的内容进行修整
4.下载视频
"""

#拉取视频的网址
url="https://pearvideo.com/video_1690368"
contId=url.split("_")[-1]
video_statusUrl=f"https://pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.16508443365382353"
resp=requests.get(video_statusUrl,headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    #防盗链
    "Referer": url
})
dic=resp.json()
srcUrl=dic['videoInfo']['videos']['srcUrl']
systemTime=dic['systemTime']
srcUrl=srcUrl.replace(systemTime,f"cont-{contId}")
#https://video.pearvideo.com/mp4/adshort/20200819/cont-1690368-15336505_adpkg-ad_hd.mp4 真
#https://video.pearvideo.com/mp4/adshort/20200819/1665051337876-15336505_adpkg-ad_hd.mp4 假
#下载视频
with open("videos/pear.mp4",mode='wb') as f:
    f.write(requests.get(srcUrl).content)
resp.close()