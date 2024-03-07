import scrapy


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["ty.lianjia.com"]
    start_urls = [f"https://ty.lianjia.com/zufang/pg{i}/#contentList" for i in range(1, 3)]

    def parse(self, response, **kwargs):
        full_url = ['https://ty.lianjia.com' + url for url in response.xpath(
            '//div[@class="content__list--item--main"]/p[@class="content__list--item--title"]/a[1]/@href').extract()]
        for item in full_url:
            yield scrapy.Request(url=item, callback=self.parse_info)

    def parse_info(self, response):
        # 房源的标题
        title = response.xpath('//div[@class="content clear w1150"]/p/text()').get().strip()
        # 房源的价格
        total_price = response.xpath(
            '//div[@class="content__aside--title"]/span/text()|//div[@class="content__aside--title"]/text()').getall()
        price = "".join(total_price).strip().replace('\n            ', '')
        # 租赁方式
        mode = response.xpath('//ul[@class="content__aside__list"]/li[1]/text()').get()
        # 房屋类型
        type = response.xpath('//ul[@class="content__aside__list"]/li[2]/text()').get()
        # 朝向楼层
        direction = response.xpath('//ul[@class="content__aside__list"]/li[1]/text()').get()
        # 是否有电梯
        elevator = response.xpath('//div[@class="content__article__info"]/ul/li[9]/text()').get()
        # 是否有车位
        parking = response.xpath('//div[@class="content__article__info"]/ul/li[11]/text()').get()
        # 是否有自来水
        water = response.xpath('//div[@class="content__article__info"]/ul/li[12]/text()').get()
        # 是否有电
        electric = response.xpath('//div[@class="content__article__info"]/ul/li[14]/text()').get()
        # 是否有燃气
        heating = response.xpath('//div[@class="content__article__info"]/ul/li[15]/text()').get()
        #print(title, price, mode, type, direction, elevator, parking, water, electric, heating)
        yield {
            'title': title,
            'price': price,
            'mode': mode,
            'type': type,
            'direction': direction,
            'elevator': elevator,
            'parking': parking,
            'water': water,
            'electric': electric,
            'heating': heating
        }
