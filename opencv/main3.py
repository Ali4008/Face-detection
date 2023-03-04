import cv2

eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")


#Video Capture
cap=cv2.VideoCapture(0)
while True:
    #cap.read returns a bool value which checks whether the frame is read correctly or not
    read,img=cap.read()
  
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    eyes=eye_cascade.detectMultiScale(gray,1.1,5)
  

    for (x,y,w,h) in eyes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),10)
        
    # imshow() – Display or Show Image.
    cv2.imshow('image',img)
    #cv2 waitkey() allows you to wait for a specific time in milliseconds 
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

#Turn of the video        
cap.release()