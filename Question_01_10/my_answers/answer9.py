import cv2
import numpy as np

img = cv2.imread("imori_noise.jpg")
H, W, C = img.shape

# Kernel_size
K_size = 3
pad = K_size // 2

out = np.zeros((H + 2 * pad, W + 2 * pad, C))
# out[0:pad, 0:pad]およびout[H + 2 * pad, W + 2 * pad]は0
out[pad:pad + H, pad:pad + W] = img.copy()

K = (1 / 16) * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

for x in range(pad, pad + W):
    for y in range(pad, pad + H):
        for c in range(C):
            out[x, y, c] = np.sum(out[x - pad:x + pad + 1, y - pad:y + pad + 1, c] * K)

cv2.imshow('image', out[pad:pad + H, pad:pad + W].astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# out[pad:pad + H, pad:pad + W] = img.copy()
# この後outを描画してもimgと一致しない!
# astype(np.uint8)が必要