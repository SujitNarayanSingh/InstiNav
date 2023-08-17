import cv2
import numpy as np
img=cv2.imread("Resource/lena.png")

cv2.imshow("car",img)

# translation
def translate(img,x,y):
    transMatrix=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv2.warpAffine(img,transMatrix,dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> left

translated = translate(img,100,100)
cv2.imshow("translated image", translated)


# rotation

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMatrix = cv2.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv2.warpAffine(img,rotMatrix, dimensions)

rotated = rotate(img,-45)
cv2.imshow("rotated",rotated)

rotated_rotated = rotate(rotated,-45)
cv2.imshow("rotated_again",rotated_rotated)


# Resizing
resized = cv2.resize(img,(500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized_image",resized)


#fliping

flip = cv2.flip(img,-1)
cv2.imshow("flipped_image",flip)
cv2.waitKey(0)

#cropping
cropped = img[200:400,300:400]
cv2.imshow("cropped_image",cropped)