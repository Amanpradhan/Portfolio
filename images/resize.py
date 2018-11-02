import cv2

im = cv2.imread('facerec1.png')
im1 = cv2.resize(im, (300, 300))
cv2.imwrite('recface.png', im1)