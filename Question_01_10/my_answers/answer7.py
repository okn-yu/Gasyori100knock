import cv2
import numpy as np

img = cv2.imread("imori.jpg")
pool_size = 8

h, w = img.shape[0], img.shape[1]

for i in range(0, h, pool_size):
    for j in range(0, w, pool_size):
        h_avg = np.average(img[i:i + pool_size, j:j + pool_size], axis=0)
        img[i:i + pool_size, j:j + pool_size] = np.average(h_avg, axis=0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
