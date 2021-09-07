import cv2
import numpy as np

resim1=cv2.imread("sogan.jpg")
resim2=cv2.imread("beyaz.png")
resim3=cv2.imread("dag.jpg")

print(resim1[120,100])
print(resim2[50,50])

cv2.imshow("Sogan Resmi",resim1)
cv2.imshow("Beyaz Resim",resim2)
birlesmis=cv2.add(resim1,resim3)
agirlikliToplama=cv2.addWeighted(resim1,0.4,resim3,0.6,0)

cv2.imshow("Agirlikli Toplama",agirlikliToplama)
cv2.imshow("Birlesmis",birlesmis)
print(resim1[120,100]+resim2[50,50])

cv2.waitKey(0)
cv2.destroyAllWindows()