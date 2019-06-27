import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape  #(128, 128, 3)

y_before = np.arange(H) # (128, )
x_before = np.arange(W) # (128, )

y_after = y_before + 30
x_after = x_before - 30

y_after = np.tile(y_after, (W, 1)) # (128, 128)
x_after = np.tile(x_after, (H, 1)) # (128, 128)

y_after[y_after < (30 + W)] = 0
x_after[x_after < -30] = 0

out = img[y_after, x_after].astype(np.uint8)

print(out.shape)

# # Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)

# 一言
# Affine変換の平行移動は定数値を足すだけだと勘違い
# 意外とはまった