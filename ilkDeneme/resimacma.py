import cv2
import numpy as np

resim=cv2.imread("logo.png",0)
cv2.imshow("ozengineer",resim)
#cv2.imwrite("yeniresim.png",resim)


print(resim.size)
print(resim.dtype) 
print(resim.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
 

