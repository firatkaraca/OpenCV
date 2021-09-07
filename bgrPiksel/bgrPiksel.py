import cv2
import numpy as np

kurtResmi=cv2.imread("kurt.jpg")
cv2.imshow("kurt",kurtResmi)


print(kurtResmi[( 230,80)])
      
print("Resmin Boyutu : "+str(kurtResmi.size))
print("Resmin Özellikleri : "+str(kurtResmi.shape))  
print("Resmin Veri Tipi : "+str(kurtResmi.dtype ))
cv2.waitKey(0)
cv2.destroyAllWindows()
 
