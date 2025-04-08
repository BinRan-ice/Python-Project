# coding:utf-8
import cv2

img=cv2.imread("../image/black.png",0)
#低于阈值零处理
t1,dst1=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow("img",img)
cv2.imshow('dst1',dst1)
cv2.waitKey()
cv2.destroyAllWindows()