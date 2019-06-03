import cv2
import numpy as np

img = cv2.imread("imori.jpg")
H, W, C = img.shape

# RGB -> HSV

B = img[:, :, 0].copy()
G = img[:, :, 1].copy()
R = img[:, :, 2].copy()

b, g, r = B / 254, G / 254, R / 254

max = img.max(axis=2)
min = img.min(axis=2)

print(max.shape)
print(min)


#Max = np.max(r, g, b)
#min = np.min(r, g, b)

# HSV -> RGB

# 一言
# 多次元配列の特定の列の最大値および最小値はaxisを使うのが定石
# 多次元配列の最大最小と軸の関係は一度整理すること
