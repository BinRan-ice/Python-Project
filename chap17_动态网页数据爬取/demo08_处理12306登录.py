# coding:utf-8
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from demo06_超级鹰 import Chaojiying_Client
import time

"""
如果你的程序被识别到了怎么办?
1.chrome的版本号如果小于88
    在你启动浏览器的时候（此时没有加载任何网页内容的时候），向页面嵌入js代码，去掉webdriver
2.chrome的版本号如果大于等于88
    option=Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument('--disable-blink-features=AutomationControlled')
"""
#1.chrome的版本号如果小于88
# driver = Chrome('./chromedriver')
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#    "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
# })
option=Options()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_argument('--disable-blink-features=AutomationControlled')

web=Chrome(options=option)
web.get("https://kyfw.12306.cn/otn/resources/login.html")
time.sleep(3)
web.find_element(By.XPATH,'//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a').click()
time.sleep(3)

"""
#如果有验证码，就先处理验证码
verify_img_element=web.find_element(By.XPATH,'Xpath地址')
#使用超级鹰识别验证码
chaojiying = Chaojiying_Client('用户名', '密码', '软件ID')
dic=chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)
result=dic['pic_str']     #x1,y1|x2,y2|x3,y3
rs_list=result.split("|")
for rs in rs_list:  #x1,y1
    p_temp=rs.split(",")
    x=int(p_temp[0])
    y=int(p_temp[1])
    #要让鼠标移动到某个位置点击
    #事件链：醒了->掀开被子->做起来->穿鞋子->穿衣服->开始执行工作
    ActionChains(web).move_to_element_with_offset(verify_img_element,x,y).click().perform()
"""

#输入用户名和密码
web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys('1137783204@qq.com')
time.sleep(3)
web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys('Lz5201314zL12306')
time.sleep(3)
#点击登录
web.find_element(By.XPATH,'//*[@id="J-login"]').click()
time.sleep(3)
#拖拽
btn=web.find_element(By.XPATH,'//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()
time.sleep(3)


