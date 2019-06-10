import cv2
import numpy as np

img = cv2.imread("imori_noise.jpg")
H, W, C = img.shape

# Kernel_size
K_size = 3
pad = K_size // 2

out = np.zeros((H + 2 * pad, W + 2 * pad, C))
out[pad:pad + H, pad:pad + W] = img.copy()

for y in range(pad, pad + W):
    for x in range(pad, pad + H):
        for c in range(C):
            out[y, x, c] = np.median(out[y - pad:y + pad + 1, x - pad:x + pad + 1, c])

cv2.imshow('image', out[pad:pad + H, pad:pad + W].astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# np.medianは中央値
# np.mean, np.averageは平均値