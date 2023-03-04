import cv2

# A classifier is the algorithm itself – the rules used by machines to classify data. A classification model, on the other hand, is the end result of your classifier's machine learning.
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#loads an image from the specified file.
img=cv2.imread("people.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
faces=face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('image',img)
    
    #cv2. waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 0 – wait indefinitely cv2.
    cv2.waitKey()