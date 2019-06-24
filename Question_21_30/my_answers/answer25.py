import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape # (128, 128, 3)
a = 1.5

# シンプルなループを用いた実装
# H_ = int(H * a)
# W_ = int(H * a)
#
# img_before = img.copy()
# img_after = np.zeros((H_, W_ , C))
#
# for h in range(H_):
#     for w in range(W_):
#         img_after[h, w] = img_before[int(h / a), int(w / a)]

# ループなしの用いた実装
aH = int(a * H)
aW = int(a * W)

# arange: 連番や等差数列を生成
# y = np.arange(aH) :0からaHまでの連番の数列を生成
# y = np.arange(aH).repeat(aW) :0をaW回、1をaW回、...、aHをaW回

y = np.arange(aH).repeat(aW).reshape(aW, -1) # y.shape: (192, 192)
x = np.tile(np.arange(aW), (aH, 1))          # x.shape: (192, 192)

y = np.round(y / a).astype(np.int)
x = np.round(x / a).astype(np.int)

# print(x[0]):  0   1   1   2   3   3   4   5   5   6   7   7   8   9   9  10  11  11 ...

img_after = img[y,x].astype(np.uint8) # out.shape: (192, 192, 3)

# Save result
cv2.imshow("result", img_after.astype(np.uint8))
cv2.waitKey(0)

# 一言
# imgの多次元配列を使う場合:
# img[index]において、indexが0次元配列のペアなら1次元配列を、1次元配列のペアなら2次元配列を、2次元配列のペアなら3次元配列を返す
