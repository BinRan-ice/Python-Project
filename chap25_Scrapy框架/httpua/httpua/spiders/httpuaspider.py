import scrapy


class HttpuaspiderSpider(scrapy.Spider):
    name = "httpuaspider"
    allowed_domains = ["httpbin.org"]
    start_urls = ["http://httpbin.org/get"]

    def parse(self, response, **kwargs):
        print(response.text)
