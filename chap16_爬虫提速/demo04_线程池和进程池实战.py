# coding:utf-8
import requests
import csv
from concurrent.futures import ThreadPoolExecutor

"""
1.如何提取单个页面的数据
2.上线程池多个页面同时抓取
"""
f=open("文件/农贸市场菜价.csv",mode="a",encoding="utf-8",newline="")
csvwriter=csv.writer(f)

def download_one_page(url,data):
    resp=requests.post(url,data=data)
    dic=resp.json()
    lst=dic['list']
    for item in lst:
        lst1=list(item.values())
        #把数据存放在文件中
        csvwriter.writerow(lst1)
    print(url,"提取完毕")
    resp.close()

if __name__ == '__main__':
    """
        for i in range(2,200):
        data={
            "limit":"20",
            "current":f"{i}",
            "pubDateStartTime":"",
            "pubDateEndTime":"",
            "prodPcatid":"",
            "prodCatid":"",
            "prodName":"",
        }
        download_one_page("http://www.xinfadi.com.cn/getPriceData.html",data)
    """

    #创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            data = {
                "limit": "20",
                "current": f"{i}",
                "pubDateStartTime": "",
                "pubDateEndTime": "",
                "prodPcatid": "",
                "prodCatid": "",
                "prodName": "",
            }
            #把下载任务提交给线程池
            t.submit(download_one_page,"http://www.xinfadi.com.cn/getPriceData.html",data)
    f.close()
    print("全部下载完毕")