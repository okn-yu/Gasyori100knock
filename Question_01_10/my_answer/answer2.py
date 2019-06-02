import cv2
import numpy as np

img = cv2.imread("imori.jpg")

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

#print(type(b))
#print(b.dtype)

Y = 0.2126 * r + 0.7152 * g + 0.0722 * b

#print(type(Y))
#rint(Y.dtype)

Y = Y.astype(np.uint8)


cv2.imshow('image', Y)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# numpyのdtypeは確認・変換ができる