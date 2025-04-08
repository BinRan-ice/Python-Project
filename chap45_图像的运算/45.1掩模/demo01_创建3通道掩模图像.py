# coding:utf-8
import cv2
import numpy as np

mask = np.zeros((150, 150, 3), np.uint8)
cv2.imshow("mask", mask)
# 将指定区域像素改为纯白像素
mask[50:100, 20:80, :] = 255
cv2.imshow("mask1", mask)
# 全部改为纯白像素
mask[:, :, :] = 255
# 将指定区域像素改为纯黑像素
mask[50:100, 20:80, :] = 0
cv2.imshow("mask2", mask)
cv2.waitKey()
cv2.destroyAllWindows()
