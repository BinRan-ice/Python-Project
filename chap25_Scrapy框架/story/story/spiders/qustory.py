import scrapy


class QustorySpider(scrapy.Spider):
    name = "qustory"
    allowed_domains = ["biqg8.com"]
    start_urls = ["https://www.biqg8.com/0_1/1.html"]

    def parse(self, response, **kwargs):
        # 解析提取数据
        title = response.xpath('//div[@class="bookname"]/h1[1]/text()').extract()[0].strip()
        content = response.xpath('string(//div[@id="content"])').extract_first().strip().replace(
            '\r\n\r\n\xa0\xa0\xa0\xa0', '').replace('。”', '。”\n')
        next_url = 'https://www.biqg8.com' + response.xpath('//div[@class="bottem1"]/a[5]/@href').extract_first()
        print(next_url)
        yield {
            'title': title,
            'content': content
        }
        yield scrapy.Request(next_url, callback=self.parse)
