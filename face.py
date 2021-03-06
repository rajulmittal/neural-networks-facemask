import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('cat.jpg',0)
blur=cv2.blur(img,(20,20))

plt.subplot(121),plt.imshow(img,) , plt.title('Original') #to convert image into grayscale
plt.subplot(122) ,plt.imshow(blur) , plt.title('Blurred')
plt.show()

