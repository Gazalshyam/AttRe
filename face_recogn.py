import numpy as np
import cv2
import os
import face_recognition
import pickle

face_cascade=cv2.CascadeClassifier("C:\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")
#using this face_cascade we will detect faces in the frame
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

#label dictionary
labels={}
with open("labels.pickle",'rb') as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}

cap =cv2.VideoCapture(0)


while(True):
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for(x,y,w,h)in faces:
        #print(x,y,w,h)
        roi_gray=gray[y:y+h,x:x+w]   #coordinates 
        roi_colr=frame[y:y+h,x:x+w]
        
        #recognize? deep learned model predict keras tenserflow scikit learn pytorch

        id_,conf=recognizer.predict(roi_gray)
        if conf>=45 :#and conf<=85:
            print(id_)
            print(labels[id_])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id_]
            color=(255,255,255)
            stroke=2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

        #image files created
        img_item="my-image.png"
        #imges="myphotu.png"
        cv2.imwrite(img_item,roi_gray)
        #cv2.imwrite(imges,roi_colr)
        
        #rectangles on faces
        color=(255,0,0)
        color_gray=(120,120,120) #BGR 0-255
        stroke=2 #thickness of line
        end_cord_x=x+w
        end_cord_y=y+h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)    #draws rectangle on face
        cv2.rectangle(gray,(x,y),(end_cord_x,end_cord_y),color_gray,stroke)

    #display the frame
    cv2.imshow('frame',frame)
    #cv2.imshow('fra',gray)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    