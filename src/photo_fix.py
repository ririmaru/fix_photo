import numpy as np
import cv2

img = cv2.imread('/Users/shimizurio/cyber/photofix/selfie.jpg')
mask = cv2.imread('/Users/shimizurio/cyber/photofix/selfie_b.jpg',0)
#cv2.imshow('img',img)
#cv2.imshow('mask',mask)

dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)

cv2.imshow('orignal',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()