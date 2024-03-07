import scrapy


class XslloginSpider(scrapy.Spider):
    name = "xsllogin"
    allowed_domains = ["xslou.com"]

    # start_urls = ["http://xslou.com/"]

    def start_requests(self):
        url = 'https://www.xslou.com/login.php'
        form_data = {
            "username": "18600605736",
            "password": "57365736",
            "usecookie": '0',
            "action": "login",
            "submit": "(unable to decode value)"
        }
        yield scrapy.FormRequest(url, formdata=form_data, callback=self.parse)

    def parse(self, response, **kwargs):
        yield scrapy.Request('https://www.xslou.com/modules/article/uservote.php?id=13', callback=self.parse_article)

    def parse_article(self, response):
        print(response.text)
