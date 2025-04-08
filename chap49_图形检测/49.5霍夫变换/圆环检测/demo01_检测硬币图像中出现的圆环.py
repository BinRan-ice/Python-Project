# coding:utf-8
import cv2
import numpy as np

img=cv2.imread("../../image/coin.jpg")   # 读取图片
o=img.copy()  # 复制原图
o=cv2.medianBlur(o,5)  # 中值滤波
gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  # 转换为灰度图
#检测圆环，圆心最小间距为70，Canny最大阈值为100，投票数超过25，最小半径为10，最大半径为50
circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,70,param1=100,param2=25,minRadius=10,maxRadius=50)
circles=np.uint(np.around(circles))  # 把circles包含的圆心和半径的值变成整数
for c in circles[0]:  # 遍历每一个圆
    x,y,r=c  # 获取圆的圆心和半径
    cv2.circle(img,(x,y),r,(0,0,255),3)  # 绘制圆
    cv2.circle(img,(x,y),2,(255,0,0),3)  # 绘制圆心
cv2.imshow("img",img)  # 显示图像
cv2.waitKey()  # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口