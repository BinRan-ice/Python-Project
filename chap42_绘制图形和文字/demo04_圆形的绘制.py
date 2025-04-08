# coding:utf-8
import numpy as np
import cv2

canvas = np.zeros((100, 300, 3), dtype="uint8")  # 创建一个空画布
canvas=cv2.circle(canvas,(50,50),40,(0,0,255),-1) # 绘制实心圆形
canvas=cv2.circle(canvas,(150,50),40,(0,255,255),-1) # 绘制实心圆形
canvas=cv2.circle(canvas,(250,50),40,(0,255,0),-1) # 绘制实心圆形
cv2.imshow("TrafficLights",canvas)  # 显示图像
cv2.waitKey()  # 等待按键按下
cv2.destroyAllWindows()  # 关闭所有窗口