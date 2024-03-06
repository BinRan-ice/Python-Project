# coding:utf-8
import requests
import json

def send_request(url):
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    resp=requests.get(url,headers=headers)
    return resp.text

def parse_json(data):
    return data.replace('fetchJSON_comment98(','').replace(');','') #结果为str类型

def type_change(data):
    return json.loads(data)

def save(jsons):
    json.dump(jsons,open("文件/京东销量最好的粽子数据.txt",mode="w",encoding="utf-8"),ensure_ascii=False)

def start(url):
    data=send_request(url)
    s=parse_json(data)
    jsons=type_change(s)
    save(jsons)

if __name__ == '__main__':
    url="https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1087591&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    start(url)