# coding:utf-8
import numpy as np
import cv2

canvas = np.zeros((100, 300, 3), dtype="uint8")  # 创建一个空画布
#文字的斜体效果
fontStyle=cv2.FONT_HERSHEY_TRIPLEX+cv2.FONT_ITALIC
cv2.putText(canvas,"mrsoft",(20,70),fontStyle,2,(0,255,0),5) # 绘制文字
cv2.imshow("canvas",canvas) # 显示图像
cv2.waitKey() # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口