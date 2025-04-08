# coding:utf-8
import cv2

image=cv2.imread("../image/image.png")
templ=cv2.imread("../image/temp.png")
height,width,c=templ.shape
results=cv2.matchTemplate(image,templ,cv2.TM_CCOEFF_NORMED) #按照标准相关系数匹配
station_Num=0
for y in range(len(results)):
    for x in range(len(results[y])):
        if results[y][x]>0.99:
            cv2.rectangle(image,(x,y),(x+width,y+height),(255,0,0),2)
            station_Num+=1
cv2.putText(image,"the numbers of stations:" + str(station_Num),(0,30),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
cv2.imshow("result",image)
cv2.waitKey()
cv2.destroyAllWindows()