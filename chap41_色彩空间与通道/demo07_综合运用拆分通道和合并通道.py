# coding:utf-8

import cv2

img = cv2.imread("image/5.1.jpg")  # 读取图像
cv2.imshow("image", img)  # 显示图像
# 将图像从BGR色彩空间转换到HSV色彩空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("image_hsv", img_hsv)  # 显示图像
h, s, v = cv2.split(img_hsv)  # 拆分图像通道
h[:,:]=180  # 将H通道的像素值设置为180
hsv=cv2.merge([h,s,v])  # 合并图像通道
brg=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)  # 将图像从HSV色彩空间转换到BGR色彩空间
cv2.imshow("image_brg", brg)  # 显示图像
cv2.waitKey()  # 等待按键按下
cv2.destroyAllWindows()  # 关闭所有窗口