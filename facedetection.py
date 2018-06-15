import cv2
faceCascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #predefined library for face detection
video_capture=cv2.VideoCapture(0)
while True:
	ret,frame=video_capture.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting frame color grom BGR to gray
	faces=faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1, #scales down the image to 10%
	minNeighbors=5,  #it lies between 3 to 6 and depicts accuracy and qualtity will increase but detection reduces on high value
	minSize=(30,30) #the maximum size of image which can be detected
	)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) #to draw the green rectangel around face of given x,y width(w) and height(h) with rgb value and '2' gives width of the boundary
	cv2.imshow('Video',frame) #to show the video

	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break
video_capture.release()
cv2.destroyAllWindows()