import cv2

img = cv2.imread("imori.jpg")

#print(img.shape) # (128, 128, 3)
#print(img[0][0]) # [132 80 67] = (B, G ,R)

# All Black img.
# img[:, :, (0, 1, 2)] = 0

# All White img.
#img[:, :, (0, 1, 2)] = 255

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 一言メモ
# 各ピクセルの（x, y）座標に対して、RGBではなくてBGR毎に値を持っている