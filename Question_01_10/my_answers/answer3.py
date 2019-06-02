import cv2
import numpy as np

img = cv2.imread("imori.jpg")

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

Y = 0.2126 * r + 0.7152 * g + 0.0722 * b

# print(Y.shape): (128, 128)

Y = Y.astype(np.uint8)
print(Y.shape)

th = 128
Y[Y < th] = 0
Y[Y >= th] = 255

"""
for a in range(Y.shape[0]):
    for b in range(Y.shape[1]):
        if Y[a][b] < 128:
            Y[a][b] = 0
        else:
            Y[a][b] = 255
"""

# print(Y.shape): (128, 128)

cv2.imshow('image', Y)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# ループ処理はイケてない。
# numpyの場合はTrueかFalseの真偽値で場合分けすること。
