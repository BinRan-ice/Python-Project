# coding:utf-8
import cv2


def overlay_img(img, img_over, img_over_x, img_over_y):
    img_h, img_w, img_p = img.shape
    img_over_h, img_over_w, img_over_c = img_over.shape
    if img_over_c <= 3:
        img_over = cv2.cvtColor(img_over, cv2.COLOR_BGR2BGRA)
    for w in range(0, img_over_w):
        for h in range(0, img_over_h):
            if img_over[h, w, 3] != 0:
                for c in range(0, 3):
                    x = img_over_x + w
                    y = img_over_y + h
                    if x >= img_w or y >= img_h:
                        break
                    img[y, x, c] = img_over[h, w, c]
    return img


smoking = cv2.imread("../image/smoking.png", cv2.IMREAD_UNCHANGED)
no_img = cv2.imread("../image/no.png", cv2.IMREAD_UNCHANGED)
cv2.imshow("smoking", smoking)
img = overlay_img(smoking, no_img, 95, 90)
cv2.imshow("no smoking", img)
cv2.waitKey()
cv2.destroyAllWindows()
