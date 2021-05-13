import cv2
cap = cv2.VideoCapture(0);
while 1:
   ret, frame = cap.read()
   print(ret)
   #cv2.imshow("video",frame)
   if cv2.waitKey() & 0xFF == ord('s'):
       print("HeyHbgbggggvgvggvgghv")
       break
cap.release()
cv2.destroyAllWindows()
print("j")
