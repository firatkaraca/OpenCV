import cv2
import numpy as np

resim=cv2.imread("nataliePortman.jpg")
resimGri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

yukseklik,genislik=resimGri.shape
print("Orijinal",yukseklik,genislik)

cv2.imshow("Orijinal",resim)
cv2.imshow("Grilestirilmis",resimGri)


cv2.waitKey(0)
cv2.destroyAllWindows()