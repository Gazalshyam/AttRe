import os
from PIL import Image
import numpy as np
import cv2
import pickle

BASE_DIR=os.path.dirname(os.path.abspath(__file__))  #path of this .py file
image_dir=os.path.join(BASE_DIR,"images_folder") #path for photos folder

face_cascade=cv2.CascadeClassifier("C:\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")
recognizer=cv2.face.LBPHFaceRecognizer_create()

current_id=0
label_ids={}
y_label=[]
x_train=[]

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path=os.path.join(root,file)
            #label=os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            label=os.path.basename(root).replace(" ","-").lower()
            #print(label,path)
            if  label not in label_ids:
                label_ids[label]=current_id
                current_id+=1
                

            id_=label_ids[label]
            #print(label_ids)
            #y_label.append(label)    #some number
            #x_train.append(path)     #verify this image and turn it into numpy array and convert into gray image

            pil_image=Image.open(path).convert("L") #.convert(l) into grayscale image

            #resizing the images 
            size=(550,550)
            final_image=pil_image.resize(size,Image.LANCZOS)
            image_array=np.array(final_image,"uint8")
            #print(image_array)   #converting every image in somesort of pixel

            #training
            faces=face_cascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=5)  #doing face detection in array

            for (x,y,w,h) in faces:
                roi=image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_label.append(id_)

#print(y_label)
#print(x_train)

#using pickle to save all labels and use it ot face_recogn.py file

with open("labels.pickle",'wb') as f:
    pickle.dump(label_ids,f)

#train the face recognization
#cv2.face.LBPH

recognizer.train(x_train,np.array(y_label))
recognizer.save("trainner.yml")


#implement recognizer in face_recogn.py file


