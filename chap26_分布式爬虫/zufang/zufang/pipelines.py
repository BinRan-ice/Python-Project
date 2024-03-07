# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class ZufangPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient('192.168.154.128',27017,username="root",password="root123456")
        self.lianjia = self.client.zufang.lianjia

    def process_item(self, item, spider):
        self.lianjia.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
