# coding:utf-8
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as ec  # 显示等待的条件
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException,ElementNotInteractableException
import time
import openpyxl

driver = Chrome()  # 创建浏览器对象


class TrainSpider(object):
    # 定义类属性
    login_url = "https://kyfw.12306.cn/otn/resources/login.html"  # 登录的页面
    profile_url = "https://kyfw.12306.cn/otn/view/index.html"  # 个人中心的网址
    left_ticket = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"  # 余票查询界面
    confirm_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"  # 确认乘车人和坐席

    # 定义init初始化方法
    def __init__(self, from_station, to_station, train_date, trains, passenger_name_lst):
        self.from_station = from_station
        self.to_station = to_station
        self.train_date = train_date
        self.station_code = self.init_station_code()  # self.init_station_code()返回的结果是一个字典
        self.trains = trains
        self.passenger_name_lst = passenger_name_lst
        self.selected_no = None
        self.selected_seat = None

    # 登陆的方法：
    def login(self):
        # 打开登录的界面：
        driver.get(self.login_url)
        WebDriverWait(driver, 1000).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]'))
        )
        WebDriverWait(driver, 1000).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[2]/a'))
        )
        driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[2]/a').click()
        WebDriverWait(driver, 10000).until(
            ec.url_to_be(self.profile_url)  # 等待直到URL成为个人中心页
        )
        print("登录成功！")

    def init_station_code(self):
        wb = openpyxl.load_workbook("文件/车站代码.xlsx")
        ws = wb.active  # 使用活动表
        lst = []  # 存储所有车站名称及代号
        for row in ws.rows:  # 遍历所有行
            sub_lst = []  # 用于存储每行中车站的名称和代号
            for cell in row:  # 遍历一行中的单元格
                sub_lst.append(cell.value)
            lst.append(sub_lst)
        # print(dict(lst))  # 将列表转换成地点类型
        return dict(lst)

    # 查询余票
    def search_ticket(self):
        # 打开查询余票的网址
        driver.get(self.left_ticket)
        # 找到出发站，到达站的隐藏的html标签
        from_station_input = driver.find_element(By.XPATH, '//*[@id="fromStation"]')
        to_station_input = driver.find_element(By.XPATH, '//*[@id="toStation"]')
        # 找到出发时间的input标签
        train_date_input = driver.find_element(By.XPATH, '//*[@id="train_date"]')
        # 根据键获取值
        from_station_code = self.station_code[self.from_station]  # 根据出发地找到出发地的代号
        to_station_code = self.station_code[self.to_station]  # 根据目的地找到目的地的代号
        # 执行JS代码
        driver.execute_script('arguments[0].value="%s"' % from_station_code, from_station_input)
        driver.execute_script('arguments[0].value="%s"' % to_station_code, to_station_input)
        driver.execute_script('arguments[0].value="%s"' % self.train_date, train_date_input)
        # 执行单击查询按钮，执行查询操作
        query_ticket_tag = driver.find_element(By.XPATH, '//*[@id="query_ticket"]')
        time.sleep(1)
        query_ticket_tag.click()
        # 解析车次,显示等待，等待tbody的出现
        WebDriverWait(driver, 1000).until(
            ec.presence_of_element_located((By.XPATH, '//tbody[@id="queryLeftTable"]/tr'))
        )
        # 筛选出有数据的tr,去掉属性为datatran的tr
        trains = driver.find_elements(By.XPATH, '//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
        is_flag = False  # 标记是否有余票
        while True:
            # 分别遍历每个车次
            for train in trains[:-1]:
                infos = train.text.replace('\n', ' ').split(" ")
                if infos[1] == '复':
                    infos = infos[0:1] + infos[2:]
                train_no = infos[0]  # 列表中索引为0的车次编号
                if train_no in self.trains:
                    # 根据键获取值     席别是一个列表
                    seat_types = self.trains[train_no]
                    for seat_type in seat_types:  # 遍历席位的列表
                        if seat_type == 'O':  # 说明是二等座
                            count = infos[9]  # 索引为9的是二等座
                            if count.isdigit() or count == "有":
                                is_flag = True
                                break
                        elif seat_type == 'M':  # 说明是一等座
                            count = infos[8]  # 索引为8的是一等座
                            if count.isdigit() or count == "有":
                                is_flag = True
                    # 判断是否有余票
                    if is_flag:
                        self.selected_no = train_no
                        # 有票就可以执行单击预定
                        order_btn = train.find_element(By.XPATH, './/a[@class="btn72"]')
                        order_btn.click()
                        return  # 退出的是遍历车次的循环

    def confirm(self):
        # 等待来到确认乘车人界面
        WebDriverWait(driver, 1000).until(
            ec.url_to_be(self.confirm_url)
        )
        # 等待乘车人标签显示出来
        WebDriverWait(driver, 1000).until(
            ec.presence_of_element_located((By.XPATH, '//ul[@id="normal_passenger_id"]/li/label'))
        )
        # 获取所有的乘车人
        passengers = driver.find_elements(By.XPATH, '//ul[@id="normal_passenger_id"]/li/label')
        for passenger in passengers:  # 分别遍历每一位乘车人
            name = passenger.text  # 获取乘车人的姓名
            if name in self.passenger_name_lst:
                passenger.click()  # label标签的单击
                if "学生" in name:
                    WebDriverWait(driver, 1000).until(
                        ec.presence_of_element_located((By.XPATH, '//*[@id="dialog_xsertcj"]/div[2]'))
                    )
                    WebDriverWait(driver, 1000).until(
                        ec.element_to_be_clickable((By.XPATH, '//*[@id="dialog_xsertcj_ok"]'))
                    )
                    driver.find_element(By.XPATH, '//*[@id="dialog_xsertcj_ok"]').click()
        # 确认席位
        seat_select = Select(driver.find_element(By.XPATH, '//*[@id="seatType_1"]'))
        seat_types = self.trains[self.selected_no]  # 根据键获取值，self.trains是要抢票车次的字典，self.select_no要抢票车次的键
        for seat_type in seat_types:
            try:
                seat_select.select_by_value(seat_type)
                self.selected_seat = seat_type  # 记录有票的作息
            except NoSuchElementException:
                continue
            else:
                break
        WebDriverWait(driver, 1000).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="submitOrder_id"]'))
        )
        # 提交订单
        submit_btn = driver.find_element(By.XPATH, '//*[@id="submitOrder_id"]')
        submit_btn.click()
        # 显示等待，等待到模式对话框窗口出现
        WebDriverWait(driver, 1000).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="content_checkticketinfo_id"]'))
        )
        # 等待按钮可以点击
        WebDriverWait(driver, 1000).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@id="qr_submit_id"]'))
        )
        submit_btn = driver.find_element(By.XPATH, '//*[@id="qr_submit_id"]')
        while submit_btn:
            try:
                submit_btn.click()
                submit_btn = driver.find_element(By.XPATH, '//*[@id="qr_submit_id"]')
            except (ElementNotVisibleException,ElementNotInteractableException):
                break
        print(f'恭喜{self.selected_no}的{self.selected_seat}抢票成功！！！')

    # 负责调用其他方法(组织其他的代码)
    def run(self):
        # 1.登录
        self.login()
        # 2.余票查询
        self.search_ticket()
        # 3.确认乘车人和订单
        self.confirm()


# 启动爬虫程序
def start():
    spider = TrainSpider('太原', '郑州', '2023-04-30', {'D3353': ['O', 'M']}, ['xx(学生)'])  # O表示二等座，M代表一等座
    spider.run()
    # spider.init_station_code()


if __name__ == '__main__':
    start()
