# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class DoubanPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active  # 获取活动表
        # 添加表头
        self.ws.append(['名称', '出版信息', '评分'])

    def process_item(self, item, spider):
        # 存储数据
        line = [item['title'], item['publish'], item['score']]
        # 将列表中的数据添加到工作表中
        self.ws.append(line)
        return item

    # 定义一个关闭的方法
    def close_spider(self, spider):
        self.wb.save('../文件/book.xlsx')
        self.wb.close()
