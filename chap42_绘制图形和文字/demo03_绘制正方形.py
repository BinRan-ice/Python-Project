# coding:utf-8
import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")  # 创建一个空画布
canvas=cv2.rectangle(canvas,(50,50),(250,250),(0,0,255),40)
canvas=cv2.rectangle(canvas,(90,90),(210,210),(0,255,0),30)
canvas=cv2.rectangle(canvas,(120,120),(180,180),(255,0,0),20)
canvas=cv2.rectangle(canvas,(140,140),(160,160),(0,255,255),-1)
cv2.imshow("canvas", canvas)  # 显示图像
cv2.waitKey()  # 等待按键按下
cv2.destroyAllWindows()  # 关闭所有窗口