import cv2
import numpy as np

resim=cv2.imread("cocukBayrami.jpg")

kesit=resim[50:150,300:400]
cv2.imshow("kesit alani",kesit)

resim[0:100,0:100 ]=kesit

resim[400:450,300:350]=(0,150,255) 

cv2.imshow("23 Nisan 1923",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()


