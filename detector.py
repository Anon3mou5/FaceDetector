import cv2
import numpy as np
import time
# data = cv2.imread("/Users/rachanar/Desktop/Screenshot 2019-10-29 at 3.28.07 PM.png")
# datagrey=cv2.cvtColor(data,cv2.COLOR_BGR2GRAY)
# face_cascade=cv2.CascadeClassifier("/Users/rachanar/Downloads/haarcascade_frontalface_default.xml")
# # face=face_cascade.detectMultiscale(datagrey,1.05,5)
# cv2.putText(data, "{}".format('6'), (20,20),
# 		cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
# cv2.rectangle(data,(10,10),(20,20),(240,0,0),3)
# cv2.imshow("legend",data)
# cv2.waitKey()
# cv2.destroyAllWindows()
video= cv2.VideoCapture(0)
a=0
z=time.time()
print(type(video))
while True:
 a=a+1
 check,frame= video.read()
 print(type(frame))
 key=cv2.waitKey(1)
 print(z)
 cv2.putText(frame, "{}".format(int(a/z)), (20,20),
		cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
 cv2.rectangle(frame,(10,10),(20,20),(240,0,0),3)
 cv2.imshow("l",frame)
 if(key == ord ('q')):
     break
video.release()
cv2.destroyAllWindows()


def finder( frame ):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("/Users/rachanar/Downloads/")
    grey= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    greys=detector(grey,1)
    for (i,rect) in greys:
            shape=predictor(grey,rect) 
            shape=face_utils.shape_to_np(shape)   