import cv2


img = cv2.imread('Resources/elonMusk.jpg')
img = cv2.resize(img, (740, 480))

cv2.imshow('Img', img)
cv2.waitKey(0)
