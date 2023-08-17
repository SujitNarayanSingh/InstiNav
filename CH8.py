import cv2

img = cv2.imread("Resource/cat.jpeg")
cv2.imshow("cat", img)

#Averaging
average = cv2.blur(img,(3,3))
cv2.imshow('average blur',average)

#gaussian blur
gauss=cv2.GaussianBlur(img,(3,3),0)
cv2.imshow("gaussian img",gauss)

#median blur
median=cv2.medianBlur(img,3)
cv2.imshow("median blur image",median)
cv2.waitKey(0)

