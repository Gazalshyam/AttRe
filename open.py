import numpy as np
import cv2

#select webcam also capture photos as vedio is collection of photo
cap=cv2.VideoCapture(0)

#changing parameter 
def make_1080p():
    cap.set(3,1920)
    cap.set(4,1080)

def make_720p():
    cap.set(3,1280)
    cap.set(4,720)

def make_480p():
    cap.set(3,640)
    cap.set(4,480)

def change_res(width,height):
    cap.set(3,width)
    cap.set(4,height)

#make_480p()     #change resolution of camera 

#rescale frame
def rescale_frame(frame,percent=75):
    scale_percent=percent
    width=int(frame.shape[1]*scale_percent/100)
    height=int(frame.shape[0]*scale_percent/100)
    dim=(width,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)


while True:
    ret,frame=cap.read()
    frame=rescale_frame(frame,percent=50)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('Frame',frame) #img show
    cv2.imshow('grayframe',gray)
    # cv2.imshow('grayframe2',hsv)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
