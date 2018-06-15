import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0) #0 is used for computer webcam for other wrbcams we use 1

while True: #while webcam is on
	ret,frame=cap.read() #reading frames
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting color to grayscale
	cv2.imshow('frame',gray) #to display frames
	if cv2.waitKey(1) & 0xFF == ord('q'): #until we enter 'q' the window does not close. 'q' is converted to hex value.waitkey() function defines the time at which the frame should be refreshed.
		break
cap.release()
cv2.destroyAllWindows()