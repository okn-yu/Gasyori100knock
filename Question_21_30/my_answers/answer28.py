import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape  #(128, 128, 3)

y_before = np.arange(H) # (128, )
x_before = np.arange(W) # (128, )

# y_before = np.arange(H).repeat(W).reshape(W, -1)
# x_before = np.tile(np.arange(W), (H, 1))

#y_before = np.tile(y_before, (W, 1)).astype(np.uint8) # (128, 128)
y_before = np.arange(H).repeat(W).reshape(W, -1)
x_before = np.tile(x_before, (H, 1)).astype(np.uint8) # (128, 128)

# print(y_before)
# print(x_before)

y_after = y_before - 30
x_after = x_before + 30

# y_after = np.tile(y_after, (W, 1)).astype(np.uint8) # (128, 128)
# x_after = np.tile(x_after, (H, 1)).astype(np.uint8) # (128, 128)

y_after[y_after > H] = 0
x_after[x_after > W] = 0
y_after[y_after < 0] = 0
x_after[x_after < 0] = 0

out = np.zeros((H+1, W+1, C), dtype=np.float32)
out[y_after, x_after] = img[y_before, x_before]

out = out.astype(np.uint8)

# # Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)

# 一言
# out = img[y_after, x_after]はNG

# 下の両者は次元は同じだが値は異なる
# その違いを説明できること
# y_before = np.arange(H).repeat(W).reshape(W, -1)
# x_before = np.tile(np.arange(W), (H, 1))
# そもそもrepeatとtileは異なる
# ふぅ、ようやく意味がわかった。。。