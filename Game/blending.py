import cv2
import numpy as np
img1 = cv2.imread('blend2.png')
img2 = cv2.imread('blend1.jpg')
dst = cv2.addWeighted(img1,0.75,img2,0.9,6)
cv2.imwrite("blend1.jpg",img2)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
