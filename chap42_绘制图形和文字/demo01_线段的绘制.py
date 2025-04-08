# coding:utf-8
import numpy as np
import cv2

canvas = np.ones((300, 300, 3), dtype="uint8")*255  # 创建一个空画布
canvas=cv2.line(canvas,(50,50),(250,50),(255,0,0),5) # 绘制线段
canvas=cv2.line(canvas,(50,150),(250,150),(0,255,0),10) # 绘制线段
canvas=cv2.line(canvas,(50,250),(250,250),(0,0,255),15) # 绘制线段
canvas=cv2.line(canvas,(150,50),(150,250),(0,255,255),20) # 绘制线段
cv2.imshow("canvas", canvas)  # 显示图像
cv2.waitKey()  # 等待按键按下
cv2.destroyAllWindows()  # 关闭所有窗口