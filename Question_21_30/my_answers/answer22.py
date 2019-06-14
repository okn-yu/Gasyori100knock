import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imori_dark.jpg")
img_1d = img.ravel()

m = np.mean(img_1d)
s = np.std(img_1d)
m0 = 128
s0 = 52

out = (s0 / s) * (img - m) + m0

# Display histogram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.show()

# Save result
cv2.imshow("result", out.astype(np.uint8))
cv2.waitKey(0)

# 一言
# 最初にravel()で1次元化すると元に戻せない
# ravel()前に変換を行いヒストグラム表示のときのみ1次元化すること
