import cv2
import numpy as np

resim1=cv2.imread("emelSayin.jpg")
resim2=cv2.imread("turkanSoray.jpg")

print(resim1[100,1000])
print(resim2[500,400])


cv2.imshow("Emel Sayin",resim1)
cv2.imshow("Turkan Soray",resim2)

print(resim1[100,1000]+resim2[500,400])


cv2.waitKey(0)
cv2.destroyAllWindows()