import cv2
import numpy as np

img = cv2.imread("imori_noise.jpg")
H, W, C = img.shape

# グレースケース化
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

Y = 0.2126 * r + 0.7152 * g + 0.0722 * b
Y = Y.astype(np.uint8)

# Kernel_size
K_size = 5
pad = K_size // 2
s = 3
K = np.zeros((K_size, K_size), dtype=np.float)

for y in range(-pad, pad + 1):
    for x in range(-pad, pad + 1):
        K[y + pad, x + pad] = (x ** 2 + y ** 2 - s ** 2) * (np.exp(-(x ** 2 + y ** 2) / (2 * (s ** 2))))

K /= (2 * np.pi * (s ** 6))
K /= K.sum()

print(K)

out = np.zeros((H + 2 * pad, W + 2 * pad), dtype=np.float)
out[pad:pad + H, pad:pad + W] = Y.copy().astype(np.float)
tmp = out.copy()

for y in range(pad, pad + H):
    for x in range(pad, pad + W):
        out[y, x] = np.sum(K * tmp[y - pad:y + pad + 1, x - pad:x + pad + 1])

cv2.imshow('image', out[pad:pad + H, pad:pad + W].astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# Pythonのrange(start, stop)は、startからstop-1までループ。紛らわしい...
# 2乗演算子は**
# K.sum()で一度正規化しないと画像が白一色となる

# import cv2
# import numpy as np
#
# # Read image
# img = cv2.imread("imori_noise.jpg")
# H, W, C = img.shape
#
# b = img[:, :, 0].copy()
# g = img[:, :, 1].copy()
# r = img[:, :, 2].copy()
#
# # Gray scale
# gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
# gray = gray.astype(np.uint8)
#
# # Gaussian Filter
# K_size = 5
# s = 3
#
# ## Zero padding
# pad = K_size // 2
# out = np.zeros((H + pad*2, W + pad*2), dtype=np.float)
# out[pad:pad+H, pad:pad+W] = gray.copy().astype(np.float)
# tmp = out.copy()
#
# ## Kernel
# K = np.zeros((K_size, K_size), dtype=np.float)
# for x in range(-pad, -pad+K_size):
#     for y in range(-pad, -pad+K_size):
#         K[y+pad, x+pad] = (x**2 + y**2 - s**2) * np.exp( -(x**2 + y**2) / (2* (s**2)))
# K /= (2 * np.pi * (s**6))
# K /= K.sum()
#
# print(K)
#
# for y in range(H):
#     for x in range(W):
#         out[pad+y, pad+x] = np.sum(K * tmp[y:y+K_size, x:x+K_size])
#
# out = out[pad:pad+H, pad:pad+W].astype(np.uint8)
#
# # Save result
# cv2.imwrite("out.jpg", out)
# cv2.imshow("result", out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()