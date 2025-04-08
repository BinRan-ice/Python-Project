# coding:utf-8
import cv2

img=cv2.imread("../image/background2.jpg")
templ=cv2.imread("../image/template.png")
height,width,c=templ.shape
results=cv2.matchTemplate(img,templ,cv2.TM_CCORR_NORMED)
print(len(results))
for y in range(len(results)):
    for x in range(len(results[y])):
        if results[y][x] >0.99:     #如果相关系数大于0.99则认为匹配成功
            cv2.rectangle(img,(x,y),(x+width,y+height),(0,0,255),2)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()
