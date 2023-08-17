import cv2 as cv

img=cv.imread('Resource/cat.jpeg')
cv.imshow('cat_image',img)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#
# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('BLur',blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow('Canny Edges',canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh',thresh)



contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')



cv.waitKey(0)