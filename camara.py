import cv2
alg="haarcascade_frontalface_default.xml"
hc=cv2.CascadeClassifier(alg)
cam=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    gi=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=hc.detectMultiScale(gi,1.3,4)
    for(x,y,z,a) in face:
        cv2.rectangle (img,(x,y),(x+z,y+a),(0,0,255),2)
    cv2.imshow("Face detection",img)
    key=cv2.waitKey(10)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()
 
