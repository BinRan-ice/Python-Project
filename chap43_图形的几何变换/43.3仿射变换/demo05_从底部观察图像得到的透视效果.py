# coding:utf-8
import cv2
import numpy as np

img=cv2.imread("../image/demo.png")    # 读取图像
rows,cols=img.shape[:2] # 获取图像的行数与列数
p1=np.zeros((4,2),dtype=np.float32) # 构建原图像的四个点的坐标
p1[0]=[0,0] # 第一个点的坐标
p1[1]=[cols-1,0] # 第二个点的坐标
p1[2]=[0,rows-1] # 第三个点的坐标
p1[3]=[cols-1,rows-1]   # 第四个点的坐标
p2=np.zeros((4,2),dtype=np.float32) # 构建变换后的四个点的坐标
p2[0]=[90,0]    # 第一个点的坐标
p2[1]=[cols-90,0] # 第二个点的坐标
p2[2]=[0,rows-1]   # 第三个点的坐标
p2[3]=[cols-1,rows-1]   # 第四个点的坐标
M=cv2.getPerspectiveTransform(p1,p2) # 获取透视变换矩阵
dst=cv2.warpPerspective(img,M,(cols,rows))    # 对图像进行透视变换
cv2.imshow("img",img)   # 显示原图像
cv2.imshow("dst",dst)   # 显示透视变换后的图像
cv2.waitKey()   # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口