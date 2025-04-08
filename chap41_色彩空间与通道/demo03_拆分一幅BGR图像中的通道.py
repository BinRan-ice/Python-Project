# coding:utf-8

import cv2

img = cv2.imread("image/5.1.jpg")  # 读取图像
cv2.imshow("image", img)  # 显示图像
b, g, r = cv2.split(img)  # 拆分图像通道
cv2.imshow("b", b)  # 显示B通道图像
cv2.imshow("g", g)  # 显示G通道图像
cv2.imshow("r", r)  # 显示R通道图像
cv2.waitKey()  # 等待按键按下
cv2.destroyAllWindows()  # 关闭所有窗口
