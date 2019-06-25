import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape # (128, 128, 3)

# astypeの有無によらずcv.imread()はndarrayを返す
#print(type(img)) #: <class 'numpy.ndarray'>

# Bi-lenear
a = 1.5
aH = int(a * H)
aW = int(a * W)

y = np.arange(aH).repeat(aW).reshape(aW, -1)
x = np.tile(np.arange(aW), (aH, 1))
y = (y / a)
x = (x / a)

# ここまではanswer25と同じ
# floorはより小さな整数値で丸める
ix = np.floor(x).astype(np.int)
iy = np.floor(y).astype(np.int)

# ixおよびiyはW-2, H-2を超えることはない
ix = np.minimum(ix, W-2) # ix.shape: (192, 192)
iy = np.minimum(iy, H-2) # iy.shape: (192, 192)

dx = x - ix # dx.shape: (192, 192)
dy = y - iy # dy.shape: (192, 192)

dx = np.repeat(np.expand_dims(dx, axis=-1), 3, axis=-1) # dx.shape: (192, 192, 3)
dy = np.repeat(np.expand_dims(dy, axis=-1), 3, axis=-1) # dy.shape: (192, 192, 3)

out = (1-dx) * (1-dy) * img[iy, ix] + dx * (1 - dy) * img[iy, ix+1] + (1 - dx) * dy * img[iy+1, ix] + dx * dy * img[iy+1, ix+1]

out[out>255] = 255
out = out.astype(np.uint8)

# Save result
# cv2.imshow("result", out)
# cv2.waitKey(0)
# cv2.imwrite("out.jpg", out)

# 一言
# READMEの説明を見ても何を言っているのかわからなかった
# コピペしてソースコードの解説を追記した