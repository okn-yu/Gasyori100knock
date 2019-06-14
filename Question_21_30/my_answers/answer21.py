import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imori_dark.jpg")

a = 0
b = 255
c = np.min(img)
d = np.max(img)
out_img = ((b - a) / (d - c)) * (img - c) + a

# Display histogram
plt.hist(out_img.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.show()

# Save result
cv2.imshow("result", out_img.astype(np.uint8))
cv2.waitKey(0)

# 一言
# 最初にravel()で1次元化すると元に戻せない
# ravel()前に変換を行いヒストグラム表示のときのみ1次元化すること
