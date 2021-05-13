import cv2
import numpy as np
frame = cv2.imread("hand1.png",-1)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_skin = np.array([0,10,10], dtype=np.uint8)
upper_skin = np.array([25,150,150], dtype=np.uint8)
       

mask = cv2.inRange(hsv, lower_skin, upper_skin)
kernel = np.ones((5,5),np.uint8)
mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
mask = cv2.dilate(mask , kernel , iterations = 3)
contours,heirarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i in range(0, len(contours)):
            if (i % 1 == 0):
                cnt = contours[i]


                x,y,w,h = cv2.boundingRect(cnt)
                if ( w*h > 2500):
                    cv2.drawContours(mask ,contours, -1, (255,0,0), 3)
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow( "dhaval",mask )
cv2.imshow( "atharva",frame )
