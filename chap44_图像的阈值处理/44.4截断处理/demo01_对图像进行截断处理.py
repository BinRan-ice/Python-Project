# coding:utf-8
import cv2

img=cv2.imread("../image/black.png",0)
t1,dst1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#截断处理
t2,dst2=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()
