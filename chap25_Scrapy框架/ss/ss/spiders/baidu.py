import scrapy
from scrapy import signals
from selenium.webdriver import Chrome


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://baidu.com/"]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaiduSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider.driver = Chrome()  # 创建完爬虫对象之后，添加一个浏览器对象
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        # 关闭浏览器对象
        spider.driver.close()

    def parse(self, response, **kwargs):
        print(response.text)
