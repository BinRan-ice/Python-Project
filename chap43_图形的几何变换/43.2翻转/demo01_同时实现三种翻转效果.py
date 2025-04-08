# coding:utf-8
import cv2

img=cv2.imread("../image/demo.png")    # 读取图像
dst1=cv2.flip(img,0)    # 水平翻转图像
dst2=cv2.flip(img,1)    # 垂直翻转图像
dst3=cv2.flip(img,-1)   # 水平垂直翻转图像
cv2.imshow("img",img)   # 显示原图像
cv2.imshow("dst1",dst1) # 显示水平翻转后的图像
cv2.imshow("dst2",dst2) # 显示垂直翻转后的图像
cv2.imshow("dst3",dst3) # 显示水平垂直翻转后的图像
cv2.waitKey()   # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口