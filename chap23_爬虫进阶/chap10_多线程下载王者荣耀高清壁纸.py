# coding:utf-8
import requests
from urllib import parse
from urllib import request
import os

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "referer": "https: // pvp.qq.com /"
    }

#发送请求
def send_request():
    url="https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=1&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1681207244035"
    resp=requests.get(url,headers=headers)
    return resp.json()

#提取请求中的链接
def parse_json(json_data):
    d={}
    data_lst=json_data["List"]
    for data in data_lst:
        image_url_lst=exact_url(data)
        sProdName=parse.unquote(data["sProdName"])
        d[sProdName]=image_url_lst
    save_jpg(d)

#解析链接为正常url
def exact_url(data):
    image_url_lst=[]
    for i in range(1,9):
        image_url=parse.unquote(data[f'sProdImgNo_{i}']).replace("200","0")
        image_url_lst.append(image_url)
    return image_url_lst

#保存图片
def save_jpg(d):
    for key in d:
        #拼接路径   王者荣耀图片/马克波罗-暗影游猎
        dirpath=os.path.join("王者荣耀图片",key.strip(" "))
        os.mkdir(dirpath)
        #下载图片并保存
        for index,image_url in enumerate(d[key]):
            request.urlretrieve(image_url,os.path.join(dirpath,"{}.jpg").format(index+1))
            print("{}下载完毕".format(d[key][index]))

#启动程序
def start():
    json_data=send_request()
    parse_json(json_data)

if __name__ == '__main__':
    start()