# coding:utf-8
import requests
import csv
import json

def send_request(url):
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    resp=requests.get(url,headers=headers)
    return resp.text

def pares_html(data):
    s=data.replace('fetchJSON_comment98(', '').replace(');', '')  # 结果为str类型
    dict_data=json.loads(s)
    comments_list=dict_data['comments']
    lst=[]
    for comment in comments_list:
        content=comment['content']  #评论的内容
        creationTime=comment['creationTime'].split(' ')[0]    #获取评论时间
        lst.append([content,creationTime])
    save(lst)

def save(lst):
    with open("文件/粽子的评论数据.csv",mode="w",encoding="utf-8",newline="") as file:
        writer=csv.writer(file)
        writer.writerows(lst)

def start(url):
    data=send_request(url)
    pares_html(data)

if __name__ == '__main__':
    url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1087591&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    start(url)