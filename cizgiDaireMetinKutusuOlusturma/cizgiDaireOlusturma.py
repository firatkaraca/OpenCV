import cv2
import numpy as np

resim=np.zeros((400,400,3),dtype="uint8")

cv2.line(resim,(100,30),(100,100),(0,0,255),3)
cv2.circle(resim,(150,150),25,(0,255,0),3)
cv2.rectangle(resim,(200,200),(250,250),(255,0,0),3)

cv2.putText(resim,"KARACA",(80,320),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),1)
cv2.imshow("Resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()