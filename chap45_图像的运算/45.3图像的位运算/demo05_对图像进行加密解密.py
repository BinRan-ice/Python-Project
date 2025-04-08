# coding:utf-8
import cv2
import numpy as np

def encode(img,img_key):
    result=cv2.bitwise_xor(img,img_key)
    return result

flower=cv2.imread("../image/amygdalus triloba.png")
rows,colmns,channel=flower.shape
#制作密钥图像
img_key=np.random.randint(0,256,(rows,colmns,3),np.uint8)
cv2.imshow("1",flower)
cv2.imshow("2",img_key)

result=encode(flower,img_key)
cv2.imshow("3",result)
result=encode(result,img_key)
cv2.imshow("4",result)
cv2.waitKey()
cv2.destroyAllWindows()