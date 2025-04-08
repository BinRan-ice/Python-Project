# coding:utf-8
import cv2

sun=cv2.imread("../image/sunset.jpg")
beach=cv2.imread("../image/beach.jpg")
rows,colmns,channel=sun.shape
beach=cv2.resize(beach,(colmns,rows))
img=cv2.addWeighted(sun,0.6,beach,0.6,0)
cv2.imshow("sun",sun)
cv2.imshow("beach",beach)
cv2.imshow("addWeighted",img)
cv2.waitKey()
cv2.destroyAllWindows()
