# coding:utf-8
import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanItem  # 导入items模块下的DoubanItem类


class DoubanSpider(scrapy.Spider):
    name = "douban"  # 定义爬虫的名称，启动爬虫程序时启用
    allowed_domains = ['book.douban.com/top250']  # 定义允许爬虫爬取的域名
    start_urls = ['https://book.douban.com/top250']  # 定义起始的网址，告诉我们的爬虫程序，应该从哪个网址开始爬取

    # parse是Scrapy里默认的处理response(响应)的一个方法
    def parse(self, response, **kwargs):
        bs = BeautifulSoup(response.text, 'html.parser')
        tr_tag = bs.find_all('tr', class_='item')
        for tr in tr_tag:
            item = DoubanItem()  # 创建DoubanItem这个类的对象
            title = tr.find_all('a')[1]['title']  # 提取书名
            publish = tr.find('p', class_='pl').text  # 提取出版信息
            score = tr.find('span', class_='rating_nums').text  # 提取评分
            # 测试打印输出
            # print([title, publish, score])
            item['title'] = title
            item['publish'] = publish
            item['score'] = score
            # 数据封装完毕以后，需要提交给引擎
            yield item
