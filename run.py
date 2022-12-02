# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 04:39:40 2022

@author: DELL
"""


import numpy as np
import cv2
import tensorflow 
from tensorflow import keras 
from tensorflow.keras.models import load_model

# load the model from disk
filename = 'vgg16.hdf5'
vgg16 = load_model(filename)

celeb_names=['Angelina Jolie', 'Bhuvan Bam', 'Brad Pitt', 'Denzel Washington', 'Hrithik Roshan', 
               'Jennifer Lawrence', 'Kate Winslet', 'Leonardo DiCaprio', 'Megan Fox', 'Natalie Portman',
               'Robert Downey Jr', 'Sandra Bullock', 'Scarlett Johansson', 'Tom Cruise', 'Tom Hanks']

font = cv2.FONT_HERSHEY_SIMPLEX
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height'''

while True:
    ret, img = cap.read()
    faces = faceCascade.detectMultiScale(
        img,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cropped_image = img[y:y+h, x:x+w] 
        IMG_SIZE=256
        color_img = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
        new_array = cv2.resize(color_img, (IMG_SIZE, IMG_SIZE))
        X=new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)
        
        pred = vgg16.predict(X)
        prediction = np.argmax(pred, axis = -1)
        confidence = np.max(pred)
        
        if (confidence*100)>60:
            
            cv2.putText(
                        img, 
                       celeb_names[prediction[0]], 
                        (x+5,y-5), 
                        font, 
                        1, 
                        (255,255,255), 
                        2
                       )
            cv2.putText(
                        img, 
                        str(confidence*100)+"%", 
                        (x+5,y+h-5), 
                        font, 
                        1, 
                        (255,255,0), 
                        1
                       )
        else:
            cv2.putText(
                        img, 
                       "Not Recognised", 
                        (x+5,y-5), 
                        font, 
                        1, 
                        (255,255,255), 
                        2
                       )
    cv2.imshow('video',img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    

cap.release()
cv2.destroyAllWindows()




