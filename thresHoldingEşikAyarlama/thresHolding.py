import cv2
import numpy as np

image=cv2.imread("image.png")
ret,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("Orijinal",image)
cv2.imshow("Thresh 1",thresh1)
cv2.imshow("Thresh 2",thresh2)
cv2.imshow("Thresh 3",thresh3)
cv2.imshow("Thresh 4",thresh4)
cv2.imshow("Thresh 5",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()
