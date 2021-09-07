import cv2
import numpy as np

resim=cv2.imread("hababamSinifi.jpg")

cv2.rectangle(resim,(250,210),(325,115),[0,0,255],2)

cv2.rectangle(resim,(400,280),(480,175),[0,255,0],2)

cv2.imshow("Hababam Sinifi",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()