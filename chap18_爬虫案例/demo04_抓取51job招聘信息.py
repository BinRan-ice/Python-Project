from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

# 安装说明:
# 1. 下载浏览器驱动. 参见"浏览器驱动.pdf"文件
# 2. 把下载好的浏览器驱动放在python解释器所在的文件夹
# 3. 下载selenium. 命令:  pip install selenium -i https://pypi.doubanio.com/simple

# 代码使用说明:
# 1. 把账号密码改成你自己的账号密码
# 2. 在当前py文件所在的文件夹内创建一个"51job"文件夹用来存放公司招聘信息

web = Chrome()

# 登录51job
web.get("https://login.51job.com/login.php")
web.maximize_window()
web.find_element(By.XPATH,'//*[@id="loginname"]').send_keys("13146297762") # 账号
web.find_element(By.XPATH,'//*[@id="password"]').send_keys("q6035945") # 密码
time.sleep(1)
# 这破网站有病. 有时候必须点两下. 原因不明
web.find_element(By.XPATH,'//*[@id="login_btn"]').click()
# web.find_element_by_xpath('//*[@id="login_btn"]').click()

# 点击职位搜索
web.find_element(By.XPATH,'//*[@id="topIndex"]/div/p/a[2]').click()

# 输入python
web.find_element(By.XPATH,'//*[@id="kwdselectid"]').send_keys("python")

# 选择地区.
web.find_element(By.XPATH,'//*[@id="work_position_input"]').click()
# 干掉所有已选地区. 更换成全国
time.sleep(1)
details = web.find_elements(By.XPATH,'ttag')
for d in details:
    d.click()
    time.sleep(1)
# 保存
web.find_element(By.XPATH,'//*[@id="work_position_click_bottom_save"]').click()
# 查询
web.find_element(By.XPATH,'/html/body/div[2]/form/div/div[1]/button').click()

while 1:
    # 找到招聘信息. 点击查看详情
    els = web.find_element(By.ID,'resultList').find_elements(By.CLASS_NAME,'el')
    for el in els:
        if "title" not in el.get_attribute("class"):
            job = el.find_element(By.CLASS_NAME,"t1").text
            company = el.find_element(By.CLASS_NAME,"t2").text
            address = el.find_element(By.CLASS_NAME,"t3").text
            salary = el.find_element(By.CLASS_NAME,"t4").text
            date = el.find_element(By.CLASS_NAME,"t5").text

            open("薪资分布数据.csv", mode="a").write(job+","+company+","+address+","+salary+","+date+"\n")
            print(1)

            # 扩展: 下载公司招聘需求, 课上代码没有下面这些
            el.find_element(By.TAG_NAME,"a").click()
            time.sleep(1)
            web.switch_to.window(web.window_handles[-1])
            company_name = web.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]').text.replace("/", "")
            job_name = web.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div[1]/h1').text.replace("/", "")
            time.sleep(1)
            # 在51job文件夹下创建"公司_职位.txt"并保存公司职位信息
            open(f"51job/{company_name}_{job_name}.txt", mode="w").write(web.find_element(By.CLASS_NAME,'job_msg').text)
            web.close()

            web.switch_to.window(web.window_handles[0])
            time.sleep(1)
            print("OK!!!!")
            # 扩展结束

    web.find_element(By.XPATH,'//*[@id="resultList"]/div[55]/div/div/div/ul/li[last()]/a').click()
    time.sleep(2)
    print("下一页!!!!")
