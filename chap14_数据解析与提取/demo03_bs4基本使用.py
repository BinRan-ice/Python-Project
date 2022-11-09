# coding:utf-8
import requests
import pandas

url="http://www.xinfadi.com.cn/getPriceData.html"
data={
    "limit": '',
    "current": '',
    "pubDateStartTime": '',
    "pubDateEndTime": '',
    "prodPcatid": '',
    "prodCatid": '',
    "prodName": '',
}
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp=requests.post(url,data=data,headers=headers)
dic=resp.json()
lst=dic['list']
df=pandas.DataFrame(lst)
df.to_csv('农贸市场菜价.csv',index=None,header=None)
resp.close()