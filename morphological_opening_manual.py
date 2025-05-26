import cv2
import numpy as np 
import matplotlib.pyplot as plt 

path = r"C:\Users\USER\Pictures\Screenshots\Screenshot 2025-03-15 161038.png"
image = cv2.imread(path)

# threshhold to get a binary image
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# kernel 
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(binary, kernel, iterations = 1) # apply erosion
opening_manual = cv2.dilate(eroded, kernel, iterations = 1) # apply dilation after erosion

cv2.imshow('Original Binary Image', binary)
cv2.imshow('Eroded Image', eroded)
cv2.imshow('Morphological Opening (Manual)', opening_manual)
cv2.waitKey(0)
