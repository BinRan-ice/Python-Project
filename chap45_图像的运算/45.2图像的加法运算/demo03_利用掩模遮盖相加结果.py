# coding:utf-8
import cv2
import numpy as np

img1=np.zeros((150,150,3),np.uint8)
#蓝色通道赋予最大值
img1[:,:,0]=255
img2=np.zeros((150,150,3),np.uint8)
#红色通道赋予最大值
img2[:,:,2]=255

img=cv2.add(img1,img2)
cv2.imshow("no mask",img)

m=np.zeros((150,150,1),np.uint8)
m[50:100,50:100,:]=255
cv2.imshow("mask",m)

img=cv2.add(img1,img2,mask=m)
cv2.imshow("use mask",img)

cv2.waitKey()
cv2.destroyAllWindows()