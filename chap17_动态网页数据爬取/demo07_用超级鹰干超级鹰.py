# coding:utf-8
import time
from demo06_超级鹰 import Chaojiying_Client
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

web=Chrome()
web.get('http://www.chaojiying.com/user/login/')

#处理验证码
img=web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('BinRan', 'lz5201314zl', '939986')
dic=chaojiying.PostPic(img,1902)
verify_code=dic['pic_str']
#向页面中填入用户名和密码
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("BinRan")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("lz5201314zl")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
time.sleep(5)
#点击登录
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
