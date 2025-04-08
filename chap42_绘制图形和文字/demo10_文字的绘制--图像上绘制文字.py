# coding:utf-8
import numpy as np
import cv2

image=cv2.imread("image/2.1.jpg")   # 读取图像
fontStyle=cv2.FONT_HERSHEY_TRIPLEX # 设置字体样式
cv2.putText(image,"Flower",(20,90),fontStyle,1,(0,255,255)) # 绘制文字
cv2.imshow("Text",image)    #显示画布
cv2.waitKey()
cv2.destroyAllWindows()