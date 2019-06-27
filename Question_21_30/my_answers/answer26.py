import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape  # (128, 128, 3)

# astypeの有無によらずcv.imread()はndarrayを返す
# print(type(img)) #: <class 'numpy.ndarray'>

# Bi-lenear
a = 1.5
aH = int(a * H)
aW = int(a * W)

y = np.arange(aH).repeat(aW).reshape(aW, -1)
x = np.tile(np.arange(aW), (aH, 1))
# このx, yは拡大元の画像の座標
y = (y / a)
x = (x / a)

# ここまではanswer25と同じ
# floorはより小さな整数値で丸める
int_x = np.floor(x).astype(np.int)
int_y = np.floor(y).astype(np.int)

# int_xおよびint_yはW-2, H-2を超えることはない
int_x = np.minimum(int_x, W - 2)  # int_x.shape: (192, 192)
int_y = np.minimum(int_y, H - 2)  # int_y.shape: (192, 192)

# dx, dyは元画像の座標に戻した場合、座標が整数であることに由来するの誤差
dx = x - int_x  # dx.shape: (192, 192)
dy = y - int_y  # dy.shape: (192, 192)

# np.expand_dims: 軸を増やして次元数を増加（ただし値の絶対数は同じ）
# a1 = np.array([1,2,3])
# a2 = np.expand_dims(a1, axis=0)
# print(a2) : [[1 2 3]]
# print(a2.shape) : (1, 3)
# a3 = np.expand_dims(a1, axis=-1)
# print(a3) : [[1]
#              [2]
#              [3]]
# print(a3.shape) : (3, 1)
# a4 = np.expand_dims(a1, axis=1)
# print(a4)
# print(a4.shape)
# print(a4) : [[1]
#              [2]
#              [3]]
# print(a4.shape) : (3, 1)

dx = np.repeat(np.expand_dims(dx, axis=-1), 3, axis=-1)  # dx.shape: (192, 192, 3)
dy = np.repeat(np.expand_dims(dy, axis=-1), 3, axis=-1)  # dy.shape: (192, 192, 3)

# img[int_y, int_x], dy, dxのサイズはすべて(192, 192, 3)
# サイズが(192, 192, 3)アダマール積を取得
out = (1 - dx) * (1 - dy) * img[int_y, int_x] + dx * (1 - dy) * img[int_y, int_x + 1] + (1 - dx) * dy * img[
    int_y + 1, int_x] + dx * dy * img[int_y + 1, int_x + 1]

out[out > 255] = 255
out = out.astype(np.uint8)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)

# 一言
# READMEの説明を見ても何を言っているのかわからなかった
# コピペしてソースコードの解説を追記した
# ようやく意味がわかった、これは初見で書くのは難しそう