import cv2
import numpy as np

image=cv2.imread("image.png",0)

#simple threshHolding
ret,thresh1=cv2.threshold(image,160,255,cv2.THRESH_BINARY)

#adaptive thresHolding

mean=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
gaussian=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Orijinal",image)
cv2.imshow("Simple Thresh Holding",thresh1)
cv2.imshow("Mean",mean)
cv2.imshow("Gaussian",gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()