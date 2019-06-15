import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imori.jpg")
H, W, C = img.shape
S = H * W * C

#out_img = np.zeros((H, W, C))
out_img = img.copy()

Z_max = np.max(img)

sum_h = 0

for i in range(0, 255):
    index = np.where(img == i)
    h_z = len(img[index])
    sum_h += h_z
    out_img[index] = (Z_max / S) * sum_h

# Display histogram
plt.hist(out_img.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.show()

# Save result
cv2.imshow("result", out_img.astype(np.uint8))
cv2.waitKey(0)

# 一言
# 度数とはその値の出現回数を指す
# ヒストグラム自体が度数分布である
# indexの個数はlen(img[index])で求める
