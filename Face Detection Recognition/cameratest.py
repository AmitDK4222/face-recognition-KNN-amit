#Test file just to detect the Face using Haar-Cascade...
import cv2

#getting camera element &webcam on use fn
cap = cv2.VideoCapture(0) # use 0 as argument default camera

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
	ret, frame = cap.read()
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	if ret == False:
		continue

	faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5) # faces is the list of tuple [ x, y, w, h] containing face part co-codinates
	print(faces) #To show the co-codinates i.e. UpperLeft Corner & LowerRight Corner.
	

	for( x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) #to get blue box around face

	cv2.imshow("Video Frame", frame)
	

	key_pressed = cv2.waitKey(1) & 0xFF #convert it into 8 bit value

	if key_pressed == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()	