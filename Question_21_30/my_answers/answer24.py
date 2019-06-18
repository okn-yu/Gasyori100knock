import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imori_gamma.jpg").astype(np.float)
c = 1
g = 2.2

img /= 255
img_out = ((1 / c) * img) ** (1 / g)
img_out *= 255

# Save result
cv2.imshow("result", img_out.astype(np.uint8))
cv2.waitKey(0)

# 一言

