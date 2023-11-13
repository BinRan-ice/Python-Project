# coding:utf-8
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#准备好参数设置
opt=Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web=Chrome(options=opt)     #把参数配置设置到浏览器中
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
#定位到下拉列表
sel_el=web.find_element(By.XPATH,'//*[@id="OptionDate"]')
#对元素进行包装，包装成下拉菜单
sel=Select(sel_el)
#让浏览器调整选项
for i in range(len(sel.options)):   #i就是每一个下拉框选项的索引位置
    sel.select_by_index(i)      #按照索引进行切换
    time.sleep(2)
    table=web.find_element(By.XPATH,'//*[@id="TableList"]/table')
    print(table.text)   #打印所有文本信息
    print("====================")
print("程序运行完毕")
web.close()

#如何拿到页面代码（经过数据加载以及js执行之后的结果的html内容）
print(web.page_source)