# coding:utf-8
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#创建浏览器
web=Chrome()
#打开浏览器，请求到拉钩
web.get("https://www.lagou.com")
#找到那个X，点击
web.find_element(By.XPATH,'//*[@id="cboxClose"]').click()
time.sleep(3)
#找到那个文本框，输入ython之后，输出回车
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)
#错误的逻辑
#web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a')
alst=web.find_elements(By.CLASS_NAME,'p-top__1F7CL')
n=1
for a in alst:
    #找到a标签并点击
    a.find_element(By.TAG_NAME,'a').click()
    time.sleep(1)
    web.switch_to.window(web.window_handles[-1])#跳转到倒数第一个窗口
    #拿到招聘信息，
    text=web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]').text#拿文本
    #把招聘信息保存在文件中
    with open(f"text/LG{n}.txt",mode="w",encoding="utf-8") as f:
        f.write(text)
    web.close()
    web.switch_to.window(web.window_handles[0])
    time.sleep(1)
    n += 1