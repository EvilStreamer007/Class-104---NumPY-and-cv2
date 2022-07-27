import cv2
import numpy as np

img = cv2.imread('/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-104/assets/poster.jpg')

cv2.imshow("Test Image:\n",img)
#print(img) - Shows the boolean form

grey_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Image converted to a grayscale:\n",grey_img)
#print(grey_img) - Shows the boolean form of the greyscaled image

#——————————————————————————————————————————————————————————————————————————————————————————

black = np.zeros([10,10])#row,column
print(black)

black[1:6,1:6] = 255
print(black)