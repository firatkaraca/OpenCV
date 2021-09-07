import cv2
import numpy as np

kemalSunal=cv2.imread("kemalSunal.jpg")

"""
for i in range(167):
    for j in range(302):
        kemalSunal[i,j]=[0,0,0]
kemalSunal[:,:,0]=50
kemalSunal[:,:,1]=200 """

kemalSunal[60:80,140:200,0]=255
kemalSunal[60:80,140:160,1]=0
kemalSunal[60:80,180:200,2]=0
print(kemalSunal.shape)

cv2.imshow("Kemal Sunal Fotografi",kemalSunal)


cv2.waitKey(0)
cv2.destroyAllWindows()
