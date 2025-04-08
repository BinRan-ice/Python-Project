# coding:utf-8
import cv2
import numpy as np

img=cv2.imread("../../image/spider.png")   # 读取图片
k=np.ones((5,5),np.uint8)  # 创建5x5的卷积核
cv2.imshow("img",img)  # 显示原图
dst=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,k)  # 形态学梯度操作
cv2.imshow("dst",dst)  # 显示形态学梯度后的图像
cv2.waitKey()  # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口