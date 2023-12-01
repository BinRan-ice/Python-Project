# coding:utf-8
import requests

url='https://www.so.com/s'
params={
    'q':'python'
}
resp=requests.get(url,params=params)
resp.encoding='utf-8'
print(resp.text)