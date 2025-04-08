# coding:utf-8
import cv2
import numpy as np

img=cv2.imread("../image/tianye.png")   # 读取图片
k=np.ones((15,15),np.uint8)   # 创建15x15的卷积核
cv2.imshow("img",img)   # 显示原图
dst=cv2.dilate(img,k)   # 膨胀操作
dst=cv2.erode(dst,k)   # 腐蚀操作
cv2.imshow("dst",dst)   # 显示膨胀后的图像
cv2.waitKey()   # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口