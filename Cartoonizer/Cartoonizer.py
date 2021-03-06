import cv2
import numpy as np

down_step = 3
bilateral_step = 7

img_rgb = cv2.imread("pp3.jpg")
print (img_rgb.shape)

img_rgb=cv2.resize(img_rgb,(800,800))

img_color = img_rgb

for _ in range(down_step):
    img_color = cv2.pyrDown(img_color)
    
for _ in range(bilateral_step):
    img_color = cv2.bilateralFilter(img_color,d=9,
                                    sigmaColor=9,
                                    sigmaSpace=7)
for _ in range(down_step):
    img_color=cv2.pyrUp(img_color)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)

img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY,
                                 blockSize=9,
                                 C=2)

img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_color, img_edge)

stack=np.hstack([img_rgb,img_cartoon])
cv2.imshow('Cartoonizer',stack)
