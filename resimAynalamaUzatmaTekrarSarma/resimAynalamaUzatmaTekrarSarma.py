import cv2
import numpy as np
 
resim=cv2.imread("adileNasit.jpg")

aynalananResim=cv2.copyMakeBorder(resim,250,250,0,0,cv2.BORDER_REFLECT)
uzatilanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)

tekrarResim=cv2.copyMakeBorder(resim,200,200,200,200,cv2.BORDER_WRAP)
sarilanResim=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value=(75,150,175))


#cv2.imshow("Adile Nasit",resim)
cv2.imshow("Aynalanan Resim",aynalananResim)
#cv2.imshow("Uzatilan Resim",uzatilanResim)
#cv2.imshow("Tekrarlanan Resim",tekrarResim)
#cv2.imshow("Sarılan Resim",sarilanResim)



cv2.waitKey(0)
cv2.destroyAllWindows()


"""
reflect yansıtmak-aynalamak
replicate uzatmak
constant sabit
"""
