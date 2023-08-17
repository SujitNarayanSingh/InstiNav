import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Resource/cat.jpeg")
cv2.imshow("cat", img)

# plt.imshow(img)
# plt.show()


# BGR to gray scale
gray  =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

# BGR to HSV
hsv  =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)

# BGR to L*a*b
lab  =cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("Lab",lab)

# bgr to rgb
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("rgb",rgb)

plt.imshow(rgb)
plt.show()

# HSV to BGR
hsv_bgr  =cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("hsv-->bgr",hsv_bgr)

cv2.waitKey(0)