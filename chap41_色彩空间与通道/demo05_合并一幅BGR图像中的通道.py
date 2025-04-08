# coding:utf-8

import cv2

img = cv2.imread("image/5.1.jpg")  # 读取图像
b, g, r = cv2.split(img)  # 拆分图像通道
bgr=cv2.merge([b,g,r]) #合并图像通道
cv2.imshow("bgr", bgr)  # 显示合并后的图像
cv2.waitKey()  # 等待按键按下
cv2.destroyAllWindows()  # 关闭所有窗口