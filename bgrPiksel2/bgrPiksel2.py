import cv2
import numpy as np

resim=cv2.imread("joker.jpg")


resim[50,30]=[255,255,255]




cv2.imshow("joker",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
