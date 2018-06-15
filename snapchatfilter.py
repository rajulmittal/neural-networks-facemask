import cv2
from PIL import Image
import numpy as np
import time
maskPath='mask.png'
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mask=Image.open(maskPath)
def mask(image):
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	faces=faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1, #scales down the image to 10%
	minNeighbors=5,  #it lies between 3 to 6 and depicts accuracy and qualtity will increase but detection reduces on high value
	minSize=(30,30) #the maximum size of image which can be detected
	)
	background=Image.fromarray(image)
	for (x,y,w,h) in faces:
		resize_mask=mask.resize((w,h),Image.ANTIALIAS)
		offset = (x,y)

		background.paste(resize_mask,offset,mask=resize_mask)
	return np.asarray(background)
cap=cv2.VideoCapture(cv2.CAP_ANY)
while True:
	ret,frame=cap.read()
	cv2.imshow('image',mask(frame))
	if cv2.waitKey(1)==27:
		break
cap.release()
cv2.destroyAllWindows()