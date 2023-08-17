import cv2
import numpy as np

img=cv2.imread("Resource/lambo.jpg")
print(img.shape)

imgResize=cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped=img[0:200,200:500]

cv2.imshow("image",img)
cv2.imshow("image resize",imgResize)
cv2.imshow("cropped image resize",imgCropped)

cv2.waitKey(0)

