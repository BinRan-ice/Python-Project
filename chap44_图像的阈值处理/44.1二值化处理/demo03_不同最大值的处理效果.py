# coding:utf-8
import cv2

#将图像读成灰度图像
img=cv2.imread("../image/black.png",0)
t1,dst1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
t2,dst2=cv2.threshold(img,127,150,cv2.THRESH_BINARY)
#二值化处理效果图
cv2.imshow('dst1',dst1)
cv2.imshow("dst2",dst2)
cv2.waitKey()
cv2.destroyAllWindows()
