#import cv2
#import numpy as np

#img=cv2.imread("Resource/lena.png")

#kernel = np.ones((5,5),np.uint8)

#imgGray=cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
#imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
#imgCanny= cv2.Canny(img,150,200)
#imgdilation=cv2.dilate(imgCanny,kernel, iterations=1)
#imgeroded=cv2.erode(imgdilation,kernel,iterations=1)

#cv2.imshow("resized image",imgResize)
#cv2.imshow("Gray Image",imgGray)
#cv2.imshow("Blur image",imgBlur)
#cv2.imshow("canny image",imgCanny)
#cv2.imshow("dialation image",imgdilation)
#cv2.imshow("eroded image", imgeroded)
#cv2.waitKey(0)


