import cv2
import numpy as np

resim1=cv2.imread("cemYilmaz.jpg")
resim2=cv2.imread("b.jpg")


print(resim1.shape)
print(resim2.shape)

cv2.imshow("Cem Yilmaz",resim1)
cv2.imshow("Yol Manzarasi",resim2)

toplam=cv2.add(resim1,resim2,1)
agirlikliToplama=cv2.addWeighted(resim1,0.3,resim2,0.7,0)
cv2.imshow("Birlesmis Foto",toplam)
cv2.imshow("Agirlikli Toplama",agirlikliToplama)

cv2.waitKey(0)
cv2.destroyAllWindows()