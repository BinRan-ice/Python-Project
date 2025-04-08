# coding:utf-8
import cv2
import numpy as np

img=cv2.imread("../image/nigella.png")   # 读取图片
k=np.ones((5,5),np.uint8)   # 创建5x5的卷积核
cv2.imshow("img",img)   # 显示原图
dst=cv2.erode(img,k)   # 腐蚀操作
dts=cv2.dilate(dst,k)   # 膨胀操作
cv2.imshow("dts",dts)   # 显示膨胀后的图像
cv2.waitKey()   # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口