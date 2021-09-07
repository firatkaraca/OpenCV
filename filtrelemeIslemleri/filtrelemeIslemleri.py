import cv2
import numpy as np

image=cv2.imread("tren.png")
meanFilter=cv2.blur(image,(3,3))
meanFilter2=cv2.blur(image,(5,5))
meanFilter3=cv2.blur(image,(7,7))

medianFilter=cv2.medianBlur(image,(3))
medianFilter2=cv2.medianBlur(image,(7))
gauss=cv2.GaussianBlur(image,(3,3),0)
gauss2=cv2.GaussianBlur(image,(5,5),0)

cv2.imshow("orijinal resim",image)
# cv2.imshow("mean filter",meanFilter)
# cv2.imshow("mean filter 5*5",meanFilter2)
# cv2.imshow("mean filter 7*7",meanFilter3)

# cv2.imshow("medianFilter",medianFilter)
# cv2.imshow("medianFilter2",medianFilter2)

cv2.imshow("gaussianBlur",gauss)
cv2.imshow("gaussianBlur2",gauss2)
cv2.waitKey(0)
cv2.destroyAllWindows() 