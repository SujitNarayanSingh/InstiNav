import cv2
import numpy as np

img = cv2.imread("Resource/cat.jpeg")
cv2.imshow("cat",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

#laplacian
lap=cv2.Laplacian(gray,cv2.CV_64F)
cv2.imshow("laplacian",lap)

#sobel
sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0)
sobely=cv2.Sobel(gray,cv2.CV_64F,0,1)
combined_sobel=cv2.bitwise_or(sobelx,sobely)

cv2.imshow("sobel x",sobelx)
cv2.imshow("sobel y",sobely)
cv2.imshow("sobel combined",combined_sobel)


cv2.waitKey(0)