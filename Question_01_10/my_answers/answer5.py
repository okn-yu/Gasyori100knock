import cv2
import numpy as np

img = cv2.imread("imori.jpg").astype(np.int) / 255 # img.shape: (128, 128, 3)
H, W, C = img.shape

# bgr -> HSV

max = img.max(axis=2).copy() # max.shape: (128, 128)
min = img.min(axis=2).copy() # min.shape: (128, 128)
min_arg = np.argmin(img, axis=2) # min_arg.shape: (128, 128)

H = np.zeros((128, 128)) # H.shape: (128, 128)

# min: blue
b_index = np.where(min_arg == 0) # 2x2 matrix
H[b_index] = 60 * (img[b_index][:, 1] - img[b_index][:, 2]) / (max[b_index] - min[b_index]) + 60
# min: green
g_index = np.where(min_arg == 1)
H[g_index] = 60 * (img[g_index][:, 2] - img[g_index][:, 0]) / (max[g_index] - min[g_index]) + 300
# min: red
r_index = np.where(min_arg == 2)
H[r_index] = 60 * (img[r_index][:, 0] - img[r_index][:, 1]) / (max[r_index] - min[r_index]) + 180
# min = max
H[np.where(max == min)] = 0

V = max.copy()       # V.shape: (128, 128)
S = (max.copy() - min.copy())  # S.Shape: (128, 128)

# Hの反転
H = (H + 180) % 360

# HSV -> bgr
C = S                             # C.shape: (128, 128)
H = H / 60                        # H.shape: (128, 128)
X = C * (1 - np.abs((H % 2) - 1)) # X.shape: (128, 128)

bgr = np.zeros((128, 128, 3))    # bgr.shape: (128, 128, 3)

index = np.where((0 <= H) & (H < 1))
bgr[:,:,0][index] = 0 + (V - C)[index]
bgr[:,:,1][index] = X[index] + (V - C)[index]
bgr[:,:,2][index] = C[index] + (V - C)[index]

index = np.where((1 <= H) & (H < 2))
bgr[:,:,0][index] = 0 + (V - C)[index]
bgr[:,:,1][index] = C[index] + (V - C)[index]
bgr[:,:,2][index] = X[index] + (V - C)[index]

index = np.where((2 <= H) & (H < 3))
bgr[:,:,0][index] = X[index] + (V - C)[index]
bgr[:,:,1][index] = C[index] + (V - C)[index]
bgr[:,:,2][index] =  (V - C)[index]

index = np.where((3 <= H) & (H < 4))
bgr[:,:,0][index] = C[index] + (V - C)[index]
bgr[:,:,1][index] = X[index] + (V - C)[index]
bgr[:,:,2][index] = 0 + (V - C)[index]

index = np.where((4 <= H) & (H < 5))
bgr[:,:,0][index] = C[index] + (V - C)[index]
bgr[:,:,1][index] = 0 + (V - C)[index]
bgr[:,:,2][index] = X[index] + (V - C)[index]

index = np.where((5 <= H) & (H < 6))
bgr[:,:,0][index] = X[index] + (V - C)[index]
bgr[:,:,1][index] = 0 + (V - C)[index]
bgr[:,:,2][index] = C[index] + (V - C)[index]

bgr[np.where(max == min)] = 0
BGR = (bgr * 255).astype(np.uint8)

cv2.imshow('image', BGR)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言
# 正直てこずった、もう1回復習を兼ねて実施する必要がある
# numpyのndarrayは値渡しなのでcopyで渡すこと
# 多次元配列を代入して扱いたい場合は()ではなく[]を用いること
# numpyの多次元配列において、[:, :, X]は[..., X]とかける
# array[index][0]は許されない（下参照）が、array[:, :, 0][index]は許される
# bgr[index][0] = X[index]は許されない
# 意味としてはどちらも同じだと思うのだけれども...
# 要はnumpyでは両辺の末尾の添字が一致しないとだめなのだろう...
