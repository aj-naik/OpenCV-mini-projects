import cv2 
  
vc = cv2.VideoCapture('video.avi') 
car = cv2.CascadeClassifier('car.xml') 
  
 
while True: 
  
    ret, frames = vc.read() 
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)  
    cars = car.detectMultiScale(gray, 1.1, 1)   
    for (x,y,w,h) in cars: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(10,20,25),2) 
    cv2.imshow('Car Detection', frames)
    if cv2.waitKey(33) == 27: 
        break

cv2.destroyAllWindows() 
