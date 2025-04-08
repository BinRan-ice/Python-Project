# coding:utf-8
import cv2

img=cv2.imread("../image/demo.png")    # 读取图像
dst3=cv2.resize(img,None,fx=1/3,fy=1/2)  # 缩放图像
dst4=cv2.resize(img,None,fx=2,fy=2)  # 缩放图像
cv2.imshow("img",img)   # 显示原图像
cv2.imshow("dst3",dst3) # 显示缩放后的图像
cv2.imshow("dst4",dst4) # 显示缩放后的图像
cv2.waitKey()   # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口