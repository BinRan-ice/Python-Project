# coding:utf-8
import numpy as np
import cv2

canvas=np.zeros((300,300,3),dtype="uint8") # 创建一个空画布
for i in range(0,28):
    center_X=np.random.randint(0,high=300) # 随机生成圆心的X坐标
    center_Y=np.random.randint(0,high=300) # 随机生成圆心的Y坐标
    radius=np.random.randint(11,high=71) # 随机生成圆的半径
    color=np.random.randint(0,high=256,size=(3,)).tolist() # 生成一个包含3个随机整数的列表（List），这些整数的取值范围在0到255之间。
    cv2.circle(canvas,(center_X,center_Y),radius,color,-1) # 绘制随机颜色的随机半径的随机圆形
cv2.imshow("canvas",canvas) # 显示图像
cv2.waitKey() # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口