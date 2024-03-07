import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LieyunItem


class LypSpider(CrawlSpider):
    name = "lyp"
    allowed_domains = ["lieyunpro.com"]
    start_urls = ["https://lieyunpro.com/latest/p1.html"]

    rules = (
        Rule(LinkExtractor(allow=r"/latest/p\d+.html"), follow=True),
        Rule(LinkExtractor(allow=r"/archives/\d+"), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath('//h1[@class="lyw-article-title-inner"]/text()').getall()
        title = ''.join(title).strip()  # 标题
        publish_time = response.xpath('//h1[@class="lyw-article-title-inner"]/span/text()').get()  # 发布时间
        author = response.xpath('//a[contains(@class,"author-name")]/text()').get()  # 作者
        content = response.xpath('//div[@class="main-text"]//text()').getall()  # 正文
        content = ''.join(content).strip()
        article_url = response.url

        # 创建item的对象
        item = LieyunItem()
        item['title'] = title
        item['author'] = author
        item['publish_time'] = publish_time
        item['content'] = content
        item['article_url'] = article_url

        yield item
