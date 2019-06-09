import cv2
import numpy as np

img = cv2.imread("imori.jpg")

# def reduce_color(val):
#     if val < 64:
#         return 32
#     elif val < 128:
#         return 96
#     elif val < 192:
#         return 160
#     elif val < 256:
#         return 224
#
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img[i][j] = ([reduce_color(a) for a in (img[i][j])])

img = (img // 64) * 64 + 32

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# //演算子は切り捨て除算


