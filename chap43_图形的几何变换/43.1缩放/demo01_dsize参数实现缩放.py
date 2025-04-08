# coding:utf-8
import cv2

img=cv2.imread("../image/demo.png")    # 读取图像
dst1=cv2.resize(img,(100,100))  # 缩放图像
dst2=cv2.resize(img,(400,400))  # 缩放图像
cv2.imshow("img",img)   # 显示原图像
cv2.imshow("dst1",dst1) # 显示缩放后的图像
cv2.imshow("dst2",dst2) # 显示缩放后的图像
cv2.waitKey()   # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口