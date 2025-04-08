# coding:utf-8
import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")  # 创建一个空画布
pts=np.array([[100,50],[200,50],[250,250],[50,250]],dtype=np.int32) # 定义多边形的顶点
canvas=cv2.polylines(canvas,[pts],True,(0,255,255),5) # 绘制闭合等腰梯形
cv2.imshow("canvas",canvas) # 显示图像
cv2.waitKey() # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口