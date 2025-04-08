# coding:utf-8
import cv2

img = []
img.append(cv2.imread("../image/image_221.png"))
img.append(cv2.imread("../image/image_222.png"))
templ = cv2.imread("../image/templ.png")
# 初始化车位编号列表的索引为-1
index = -1
min = 1
for i in range(0, len(img)):
    results = cv2.matchTemplate(img[i], templ, cv2.TM_SQDIFF_NORMED)
    print(any(results[0]))
    if min > any(results[0]):
        index = i
cv2.imshow("result", img[index])
cv2.waitKey()
cv2.destroyAllWindows()
