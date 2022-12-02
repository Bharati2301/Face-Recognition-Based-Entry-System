# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 00:52:54 2022

@author: DELL
"""


import os


folder = "C:/Users/DELL/Downloads/ANN PROJ/FINAL DATASET/Hrithik Roshan"
for count, filename in enumerate(os.listdir(folder)):
    dst = f"HrithikRoshan_{str(count)}.jpg"
    src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst =f"{folder}/{dst}"
     
    # rename() function will
    # rename all the files
    os.rename(src, dst)