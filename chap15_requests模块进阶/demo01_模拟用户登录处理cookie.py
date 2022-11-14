# coding:utf-8
import requests

"""
1.登录->得到cookie
2.带着cookie去请求到书架url->得到书架上的内容
3.必须把上面的两个操作连接起来
4.我们可以使用session进行请求->session可以认为是一连串的请求，在这个过程中的cookie不会丢失
"""

#会话
session=requests.session()
data={
"loginName": "",
"password": ""
}

#1.登录
url="https://passport.17k.com/ck/user/login"
session.post(url,data=data)
#print(resp.cookies)        #查看cookie

#2.拿书架上的数据
#刚才的session中是有cookie的
resp=session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
"""
或者：
resp=requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919",headers={
    "Cookie": "GUID=01a1bdc8-c6d0-4177-99da-1f9577194f9e; Hm_lvt_9793f42b498361373512340937deb2a0=1665047513; sajssdk_2015_cross_new_user=1; __bid_n=1837dc78fb95c1079d4207; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F01%252F61%252F84%252F98798461.jpg-88x88%253Fv%253D1665048438000%26id%3D98798461%26nickname%3D%25E4%25B9%25A6%25E5%258F%258B28qMc6m2k%26e%3D1680600459%26s%3D7b5b584aa1653ef0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2298798461%22%2C%22%24device_id%22%3A%22183ac90c648df3-0e40039736dde8-26021f51-1327104-183ac90c649e33%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2201a1bdc8-c6d0-4177-99da-1f9577194f9e%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1665049025"
})
"""
print(resp.json())
resp.close()

