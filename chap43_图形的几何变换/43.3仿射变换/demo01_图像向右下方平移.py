# coding:utf-8
import cv2
import numpy as np

img=cv2.imread("../image/demo.png")    # 读取图像
rows,cols=img.shape[:2] # 获取图像的行数与列数
M=np.float32([[1,0,50],[0,1,100]])   # 构建平移矩阵
dst=cv2.warpAffine(img,M,(cols,rows))    # 对图像进行平移
cv2.imshow("img",img)   # 显示原图像
cv2.imshow("dst",dst)   # 显示平移后的图像
cv2.waitKey()   # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口