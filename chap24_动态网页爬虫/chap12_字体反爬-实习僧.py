# coding:utf-8
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


def send_request():
    url = "https://www.shixiseng.com/interns?keyword=python&city=%E5%85%A8%E5%9B%BD&type=intern"
    resp = requests.get(url, headers=headers)
    return resp.text


def parse_html(html):
    bs = BeautifulSoup(html, "html.parser")
    offices = bs.select('.intern-wrap.intern-item')
    for offer in offices:
        url = offer.select('.f-l.intern-detail__job a')[0]['href']
        detail_url(url)


def detail_url(url):
    html = requests.get(url, headers=headers)
    # 继续解析
    bs = BeautifulSoup(html.text, 'html.parser')
    title = bs.title.text  # 招聘的职位信息
    # 获取公司名称
    company_name = bs.select('.com_intro .com-name')[0].text.split()[0]
    # 获取薪水
    salary = bs.select('.job_money.cutom_font')[0].text
    """
    如果对数字进行了编码，则用一下代码处理：
    salary = bs.select('.job_money.cutom_font')[0].text.encode("utf-8")
    salary = salary.replace(b'\xee\xa0\x82', b'1')
    salary = salary.replace(b'\xef\x8a\x9a', b'5')
    salary = salary.replace(b'\xee\xb7\x89', b'0')
    salary = salary.replace(b'\xee\xaf\x9e', b'2')
    salary = salary.replace(b'\xee\xbb\xb6', b'3')
    salary = salary.replace(b'\xef\x9b\x98', b'8')
    salary = salary.replace(b'\xef\x98\x8c', b'4')
    salary=salary.decode("utf-8")
    """
    print(salary)


if __name__ == '__main__':
    html = send_request()
    parse_html(html)
