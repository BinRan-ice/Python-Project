# coding:utf-8
import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")  # 创建一个空画布
center_X=int(canvas.shape[1]/2) # 获取画布中心点的X坐标
center_Y=int(canvas.shape[0]/2) # 获取画布中心点的Y坐标
for r in range(0,150,30):
    canvas=cv2.circle(canvas,(center_X,center_Y),r,(255,255,0),2) # 绘制同心圆
cv2.imshow("canvas",canvas) # 显示图像
cv2.waitKey() # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口