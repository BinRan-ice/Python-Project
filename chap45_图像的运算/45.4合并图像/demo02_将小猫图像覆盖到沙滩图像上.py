# coding:utf-8
import cv2

beach_img=cv2.imread("../image/beach.jpg")
cat_img=cv2.imread("../image/cat.jpg")
cat=cat_img[75:400,120:260,:]
cat=cv2.resize(cat,(70,160))
cv2.imshow("cat",cat_img)
cv2.imshow("cat2",cat)
cv2.imshow("beach",beach_img)
rows,colmns,channel=cat.shape
beach_img[100:100+rows,260:260+colmns,:]=cat
cv2.imshow("beach2",beach_img)
cv2.waitKey()
cv2.destroyAllWindows()