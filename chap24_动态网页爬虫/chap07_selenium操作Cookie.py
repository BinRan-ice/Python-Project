# coding:utf-8
from selenium.webdriver import Chrome

# 构造浏览器
driver = Chrome()
driver.get("https://www.baidu.com/")

# (1)获取所有的cookie信息
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)
print("*" * 50)

# (2)获取指定的cookie信息
cookie = driver.get_cookie('BA_HECTOR')
print(cookie)
print("*" * 50)

# (3)添加cookie信息
driver.add_cookie({'name': 'zhangsan', 'value': '8888'})
print(driver.get_cookie("zhangsan"))
print("*" * 50)

# (4)删除cookie
driver.delete_cookie('zhangsan')
print(driver.get_cookie('zhangsan'))
print("*" * 50)

# (5)删除所有的cookie信息
driver.delete_all_cookies()  # 删除浏览器端的所有cookie信息
print(driver.get_cookies())
