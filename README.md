# Face-Recognition-Based-Entry-System


## OBJECTIVE
Face recognition liveness detection attendance systems may totally automate the manual or biometric monitoring of entry and departure times. There is no need for human involvement or physical confirmation, since the system’s powerful algorithms can autonomously find and recognize faces. Face recognition makes it easy to monitor workers’ hours worked.

## STEPS INVOLVED IN FACE RECOGNITION MODEL
1.	Face Detection: Locate faces and draw bounding boxes around faces and keep the coordinates of bounding boxes.
2.	Face Alignments: Normalize the faces to be consistent with the training database.
3.	Feature Extraction: Extract features of faces that will be used for training and recognition tasks.
4.	Face Recognition: Matching of the face against one or more known faces in a prepared database.


## STEPS FOR PRE-PROCESSING AND MODELLING

* Webscraped for photos of 15 celebrities using bing-image-downloader. 
* We cropped the images by drawing bounding boxes around the faces and saving this part of the image. Follwed by manually cleaning these as some of them were redundant. Few After this we have approximately 1500 images in total.
* For preprocessing we resize the images and convert them into arrays. For machine learning models and ANN we converted the images to GraySCale images. We split the dataset into a train-test with 80-20%.
* We used PCA for dimension reduction and to find underlying correlations that exist in a (potentially very large) set of variables.So, to sum up, the idea of PCA is simple — reduce the number of variables of a data set, while preserving as much information as possible.  Ahead we basically compare if applying PCA increases the accuracy of our model.
* First we tried out a simple Artificial Neural Network. It gave us an accuracy of only 30%. We then applied PCA and then tried ANN. This boosted our accuracy to 56%.
* KNN: Simply put, the k-NN algorithm classifies unknown data points by finding the most common class among the k-closest examples.
* SVM: A SVM algorithm generates a decision surface separating the two classes. For face recognition, we re-interpret the decision surface to produce a similarity metric between two facial images. This allows us to construct face-recognition algorithms. 
* Accuracy for KNN wasn’t good at 38% But SVM with PCA worked fine with an accuracy of 63%
* Finally we used VGG16, a renowned classification model for ImageNet classification with more than 14 million images and 1000 classes. The VGG-16 is one of the most popular pre-trained models for image classification.

## DEMONSTRATION

<p align="center">
  <img src="https://user-images.githubusercontent.com/31125521/57297377-bfcdfd80-70cf-11e9-8afa-2044cb167bff.gif">
</p>

## USE CASES

1. Finding Missing Person
2. Retail Crime
3. Security Identification
4. Identifying accounts on social media
5. School Attendance System
6. Recognizing Drivers in Cars
