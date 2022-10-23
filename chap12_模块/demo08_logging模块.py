# coding:utf-8
import logging

"""
filename:文件名
format:数据的格式化输出，最终在日志文件中的样子
        时间-名称-级别-模块：错误信息
datefmt:时间的格式
level：错误的级别权重，当错误的级别权重大于等于level的时候才会写入文件
"""
logging.basicConfig(filename='x1.txt',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=10)   #记录文件中的日志的最低等级

logging.log(10,"你好，我叫周杰伦")

#logging日志记录
logging.critical("今天系统炸了，请程序员来调试")      #最高级别的日志信息50
logging.error("一般指的是不同的程序错误，速成bug")     #40
logging.warning("我只是一个警告的消息")              #30
logging.info("我只是一个普通的消息")                 #20
logging.debug("默认最低等级的消息")                  #10


#如果想要把日志记录在不同的文件
#创建一个操作日志的对象logger（依赖FileHandler）
file_handler=logging.FileHandler("l1.log","a",encoding="utf-8")
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s"))
logger1=logging.Logger("财务系统",level=40)     #创建日志对象
logger1.addHandler(file_handler)
logger1.error('我是A系统')
#再创建一个操作日志的对象（依赖FileHandler）
file_handler2=logging.FileHandler("l2.log","a",encoding="utf-8")
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s"))
logger2=logging.Logger("会计系统",level=40)     #创建日志对象
logger2.addHandler(file_handler2)
logger2.error('我是B系统')

#项目1：财务系统出错了
logger1.error('财务系统炸了，程序员出来工作了')
#项目2：会计系统出错了
logger2.error("会计系统出错了，领导出来溜达溜达")

logger1.log(9999,"没事儿")