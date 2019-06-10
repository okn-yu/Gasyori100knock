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

out = np.zeros((H + 2 * pad, W + 2 * pad), dtype=np.float)
out[pad:pad + H, pad:pad + W] = Y.copy().astype(np.float)

tmp = out.copy()

for y in range(pad, pad + H):
    for x in range(pad, pad + W):
            max = np.max(tmp[y - pad:y + pad + 1, x - pad:x + pad + 1])
            min = np.min(tmp[y - pad:y + pad + 1, x - pad:x + pad + 1])
            out[y, x] = max - min

cv2.imshow('image', out.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# グレイスケースの252.0と252は扱いが異なる。
# 前者は白画像として表示される
# 後者は濃淡が正しく表示される
# フィルタ中にtmpの代わりにoutをそのまま用いると計算途中に元画像が更新されてしまう
# 必ずtmpを用いること！（実はこれまでもすべて同じ話が当てはまるので修正が必要...）