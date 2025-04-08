# coding:utf-8
import numpy as np
import cv2
import time

width,height=200,200    # 设置画布的宽度和高度
r=20    # 设置圆的半径
x=r+20  # 设置圆的横坐标初始位置
y=r+100  # 设置圆的纵坐标初始位置
x_offer=y_offer=4   # 设置圆的每一帧的移动速度
while cv2.waitKey(1)==-1:   # 按下任意键之后
    if x>width-r or x<r:    # 到达画布的左右边界
        x_offer=-x_offer    # 水平方向反向移动
    if y>height-r or y<r:   # 到达画布的上下边界
        y_offer=-y_offer    # 垂直方向反向移动
    x+=x_offer  # 水平方向移动
    y+=y_offer  # 垂直方向移动
    canvas=np.zeros((width,height,3),dtype="uint8")*255 # 创建一个空画布
    cv2.circle(canvas,(x,y),r,(255,0,0),-1) # 绘制实心圆形
    cv2.imshow("canvas",canvas) # 显示图像
    time.sleep(1/60)    # 设置每秒钟的帧数
cv2.destroyAllWindows() # 关闭所有窗口