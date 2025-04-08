# coding:utf-8
import numpy as np
import cv2

canvas=np.zeros((300,300,3),dtype="uint8") # 创建一个空画布
canvas=cv2.rectangle(canvas,(50,50),(200,150),(255,255,0),-1)   #绘制实心矩形
cv2.imshow("canvas",canvas) # 显示图像
cv2.waitKey() # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口