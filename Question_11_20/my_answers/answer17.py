import cv2
import numpy as np

img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape

# グレースケース化
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

Y = 0.2126 * r + 0.7152 * g + 0.0722 * b
Y = Y.astype(np.uint8)

# Kernel_size
K_size = 3
pad = K_size // 2
K_v = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

out_v = np.zeros((H + 2 * pad, W + 2 * pad), dtype=np.float)
out_v[pad:pad + H, pad:pad + W] = Y.copy().astype(np.float)

tmp = out_v.copy()

for y in range(pad, pad + H):
    for x in range(pad, pad + W):
            out_v[x, y] = np.sum(tmp[x - pad:x + pad + 1, y - pad:y + pad + 1] * K_v)


out_v[out_v < 0] = 0
out_v[out_v > 255] = 255

cv2.imshow('image', out_v.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# フィルタが正規化されていないので画素が0以下や255以上の値を取る場合がある
# そのため上限下限値の設定が必要