import cv2

img=cv2.imread("Resource/persons.jpg")
cv2.imshow("person",img)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray person",gray)

haar_cascade = cv2.CascadeClassifier('haar_faces.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)

print(f'NUmber of faces found= {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=1)

cv2.imshow('detected faces', img)
cv2.waitKey(0)