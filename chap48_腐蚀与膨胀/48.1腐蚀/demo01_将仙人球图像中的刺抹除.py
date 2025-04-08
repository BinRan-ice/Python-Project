# coding:utf-8
import cv2
import numpy as np

img=cv2.imread("../image/cactus.jpg")   # 读取图片
k=np.ones((3,3),np.uint8)  # 创建3x3的卷积核
cv2.imshow("img",img)  # 显示原图
dst=cv2.erode(img,k)  # 腐蚀操作
cv2.imshow("erode",dst)  # 显示腐蚀后的图像
cv2.waitKey()
cv2.destroyAllWindows()