import cv2
import numpy as np

# image=cv2.imread("ozg.png")

# kernel=np.ones((5,5),np.uint8)

# dilation=cv2.dilate(image,kernel,iterations=1)
# erosion=cv2.erode(image,kernel,iterations=1)

# cv2.imshow("orijinal",image)
# cv2.imshow("dilation",dilation)
# cv2.imshow("erotion",erosion)


image=cv2.imread("ozg.png")

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(image,kernel,iterations=1)
dilation=cv2.dilate(erosion,kernel,iterations=1)

opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
gradyan=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("Orijinal",image)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
cv2.imshow("Gradyan",gradyan)
cv2.imshow("Tophat",tophat)
cv2.imshow("Blackhat",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()