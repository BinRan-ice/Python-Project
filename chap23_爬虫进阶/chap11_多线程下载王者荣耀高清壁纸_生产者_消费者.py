# coding:utf-8
import requests
from urllib import parse
from queue import Queue
import threading
import os
from urllib import request

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "referer": "https: // pvp.qq.com /"
}


# 解析链接为正常url
def exact_url(data):
    image_url_lst = []
    for i in range(1, 9):
        image_url = parse.unquote(data[f'sProdImgNo_{i}']).replace("200", "0")
        image_url_lst.append(image_url)
    return image_url_lst


# 生产者线程
class Producer(threading.Thread):
    def __init__(self, page_queue, image_url_queue):
        super().__init__()
        self.page_queue = page_queue
        self.image_url_queue = image_url_queue

    def run(self) -> None:
        while not self.page_queue.empty():
            page_url = self.page_queue.get()
            resp = requests.get(page_url, headers=headers)
            json_data = resp.json()
            d = {}
            data_lst = json_data["List"]
            for data in data_lst:
                image_url_lst = exact_url(data)
                sProdName = parse.unquote(data["sProdName"])
                d[sProdName] = image_url_lst
            for key in d:
                # 拼接路径   王者荣耀图片/马克波罗-暗影游猎
                dirpath = os.path.join("王者荣耀图片", key.strip(" ").replace("·","").replace("1:1",''))
                if not os.path.exists(dirpath):
                    os.mkdir(dirpath)
                # 下载图片并保存
                for index, image_url in enumerate(d[key]):
                    # 生产图片的url
                    self.image_url_queue.put(
                        {"image_path": os.path.join(dirpath, '{}.jpg').format(index + 1), "image_url": image_url})


# 消费者线程
class Customer(threading.Thread):
    def __init__(self, image_url_queue):
        super().__init__()
        self.image_url_queue = image_url_queue

    def run(self) -> None:
        while True:
            try:
                image_obj = self.image_url_queue.get(timeout=20)
                request.urlretrieve(image_obj['image_url'], image_obj["image_path"])
                print(f"{image_obj['image_path']}下载完成")
            except:
                break


# 定义一个启动线程的函数
def start():
    page_queue = Queue(33)
    image_url_queue = Queue(1000)
    for i in range(0, 1):
        page_url = f"https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={i}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1681207244035"
        page_queue.put(page_url)
    # 创建生产者线程对象
    for i in range(5):
        t = Producer(page_queue, image_url_queue)
        t.start()
    # 创建消费者线程
    for i in range(10):
        t = Customer(image_url_queue)
        t.start()


if __name__ == '__main__':
    start()
