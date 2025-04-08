# coding:utf-8
import cv2

def myMatchTemplate(img,templ):
    height,width,c=templ.shape
    results=cv2.matchTemplate(img,templ,cv2.TM_CCOEFF_NORMED)
    loc=list()
    for i in range(len(results)):
        for j in range(len(results[i])):
            if results[i][j]>0.99:
                loc.append((j,i,j+width,i+height))
    return loc

image=cv2.imread("../image/background2.jpg")
templs=list()
templs.append(cv2.imread("../image/template.png"))
templs.append(cv2.imread("../image/template2.png"))
templs.append(cv2.imread("../image/template3.png"))
loc=list()      #所有模板匹配成功为止的红框坐标列表
for t in templs:
    loc+=myMatchTemplate(image,t)
for i in loc:
    cv2.rectangle(image,(i[0],i[1]),(i[2],i[3]),(0,0,255),2)
cv2.imshow("img",image)
cv2.waitKey()
cv2.destroyAllWindows()
