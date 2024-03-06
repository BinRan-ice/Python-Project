# coding:utf-8
import requests
from bs4 import BeautifulSoup
import mysql.connector

class LianJiaSprider():
    mydb=mysql.connector.connect(host="192.168.154.128", user="root", passwd="root123456", database="python数据库",
                            port=3309)
    mycursor=mydb.cursor()

    def __init__(self):
        self.url="https://bj.lianjia.com/ershoufang/pg{0}/"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }

    def send_request(self,url):
        resp=requests.get(url,headers=self.headers)
        if resp.status_code==200:
            return resp

    def parse_html(self,resp):
        lst=[]
        html=resp.text
        bs=BeautifulSoup(html,"lxml")
        ul=bs.find("ul",class_="sellListContent")
        li_list=ul.find_all('li')
        for item in li_list:
            title1=item.find('div',class_="title")
            title=title1.find('a',target="_blank").text
            houseInfo=item.find('div',class_="houseInfo").text
            number=item.find("div",class_="totalPrice totalPrice2").text.lstrip()
            unitPrice=item.find("div",class_="unitPrice").text
            lst.append((title,houseInfo,number,unitPrice))
        #print(lst)
        self.save(lst)

    def save(self,lst):
        #print(self.mydb)
        sql='insert into tb_lianjia (title,houseInfo,totalPrice,unitPrice) values (%s,%s,%s,%s)'
        self.mycursor.executemany(sql,lst)
        self.mydb.commit()
        print(self.mycursor.rowcount,"插入完毕")

    def start(self):
        for i in range(1,10):
            full_url=self.url.format(i)
            resp=self.send_request(full_url)
            self.parse_html(resp)

if __name__ == '__main__':
    lianjia=LianJiaSprider()
    lianjia.start()