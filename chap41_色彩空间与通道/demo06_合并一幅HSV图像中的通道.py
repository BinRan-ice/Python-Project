# coding:utf-8

import cv2

img = cv2.imread("image/5.1.jpg")  # 读取图像
# 将图像从BGR色彩空间转换到HSV色彩空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)  # 拆分图像通道
hsv=cv2.merge([h,s,v])  # 合并图像通道
bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)  # 将图像从HSV色彩空间转换到BGR色彩空间
cv2.imshow("image", bgr)  # 显示图像
cv2.waitKey()  # 等待按键按下
cv2.destroyAllWindows()  # 关闭所有窗口
