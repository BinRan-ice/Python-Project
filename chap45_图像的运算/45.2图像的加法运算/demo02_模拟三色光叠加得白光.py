# coding:utf-8
import cv2
import numpy as np

img1=np.zeros((150,150,3),np.uint8)
#蓝色通道赋予最大值
img1[:,:,0]=255
img2=np.zeros((150,150,3),np.uint8)
#绿色通道赋予最大值
img2[:,:,1]=255
img3=np.zeros((150,150,3),np.uint8)
#红色通道赋予最大值
img3[:,:,2]=255
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("img3",img3)
img=cv2.add(img1,img2)
cv2.imshow("1+2",img)
img=cv2.add(img,img3)
cv2.imshow("1+2+3",img)
cv2.waitKey()
cv2.destroyAllWindows()