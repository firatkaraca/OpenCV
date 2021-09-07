import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    cv2.line(goruntu,(0,0),(100,100),(0,0,255),3)
    cv2.rectangle(goruntu,(100,100),(200,200),(50,50,50),3)
   
    cv2.circle(goruntu,(150,150),50,(0,255,0),3)
    cv2.putText(goruntu,"KARACA",(250,250),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),1)
    cv2.imshow("Lenovo",goruntu)
 
    if cv2.waitKey(30) & 0xFF==('q'):
        break

kamera.release()
cv2.destroyAllWindows()