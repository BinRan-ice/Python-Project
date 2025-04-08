# coding:utf-8
import cv2
import numpy as np

flower=cv2.imread("../image/amygdalus triloba.png")
mask=np.zeros(flower.shape,np.uint8)
#建立十字白色区域
mask[120:180,:,:]=255
mask[:,80:180,:]=255
img=cv2.bitwise_xor(flower,mask)
cv2.imshow("flower",flower)
cv2.imshow("mask",mask)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()