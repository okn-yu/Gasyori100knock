import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imori_dark.jpg")

H, W, C = img.shape
S = H * W * C

Z_max = np.max(img)

print(Z_max)

# Display histogram
# plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
# plt.show()

# Save result
# cv2.imshow("result", out.astype(np.uint8))
# cv2.waitKey(0)

# 一言
# 度数とはその値の出現回数を指す
# ヒストグラム自体が度数分布である
