import cv2
import numpy as np

resim=cv2.imread("nataliePortman.jpg")
ikiKatBuyuk=cv2.pyrUp(resim)

ikiKatKucuk=cv2.pyrDown(resim)

cv2.imshow("Natalie Portman",resim)
cv2.imshow("Iki Kat Buyuk",ikiKatBuyuk)
cv2.imshow("Iki Kat Kucuk",ikiKatKucuk)

print("Orijinal Resim",resim.shape)
print("Iki kat buyuk resim",ikiKatBuyuk.shape)
print("Iki kat kucuk resim",ikiKatKucuk.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()