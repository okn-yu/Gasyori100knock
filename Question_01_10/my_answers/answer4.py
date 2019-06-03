import cv2
import numpy as np

img = cv2.imread("imori.jpg")
H, W, C = img.shape

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

Y = 0.2126 * r + 0.7152 * g + 0.0722 * b
Y = Y.astype(np.uint8)

max_th = 0
max_Sb_2 = 0

for th in range(0, 255):
    s0 = (Y < th)
    s1 = (Y >= th)
    S0_list = Y[s0]
    S1_list = Y[s1]

    w0 = np.count_nonzero(s0) / (H * W)
    w1 = np.count_nonzero(s1) / (H * W)
    M0 = np.mean(S0_list) if len(S0_list) > 0 else 0
    M1 = np.mean(S1_list) if len(S1_list) > 0 else 0

    Sb_2 = w0 * w1 * ((M0 - M1) * (M0 - M1))

    if max_Sb_2 < Sb_2:
        max_th = th
        max_Sb_2 = Sb_2

print(max_th)

Y[Y < max_th] = 0
Y[Y >= max_th] = 255

cv2.imshow('image', Y)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# H, W, Cはshapeで取ること
# Pythonでも倒置ifは使える