# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:49:50 2022

@author: DELL
"""
import cv2
import sys
import os
from os import listdir


# Get user supplied values
main_folder_dir = 'C:/Users/DELL/Downloads/ANN PROJ/Scraped Data/Celebrity Faces Dataset'
list_names=[]
for celeb_name in os.listdir(main_folder_dir):
    list_names.append(celeb_name)

print(list_names)

cascPath = "haarcascade_frontalface_default.xml"
for celeb in list_names:
    print("Celeb:",celeb)
    folder_dir= main_folder_dir+'/'+celeb
    
    final_path='C:/Users/DELL/Downloads/ANN PROJ/FINAL DATASET/'+celeb
    os.mkdir(final_path)
    
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    
    i=0
    for image_name in os.listdir(folder_dir):
        i+=1
        # check if the image ends with png or jpg or jpeg
        if (image_name.endswith(".png") or image_name.endswith(".jpg")\
            or image_name.endswith(".jpeg")):
            
            # Read the image
            image = cv2.imread(folder_dir+'/'+image_name)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
            
            
            j=0
            for (x, y, w, h) in faces:
                j+=1
                #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cropped_image = image[y:(y+h), x:(x+w)]
                cv2.imwrite(final_path+"/"+celeb+"_"+str(i)+"."+str(j)+".jpg", cropped_image)
    
