"""
LGMVIP - DataScience
Beginner Level Task
Task 3: Image to Pencil Sketch with Python
Author: Om Kolte

"""

import cv2

# Read the image
img = cv2.imread('car.jpg')
cv2.imshow('Original Image', img)

# convert image into grayscale image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscaled Image', gray_image)

# invert the grayscale image (negative image)
inverted_gray_image = 255 - gray_image
cv2.imshow('Inverted Grayscaled Image', inverted_gray_image)

# blur the grayscale image and invert the blurred grayscale image
blurred_img=cv2.GaussianBlur(inverted_gray_image, (21, 21),0)
inverted_blurred_img = 255 - blurred_img
cv2.imshow('Inverted Blurred Grayscaled Image', inverted_blurred_img)

# create pencil sketch by mixing the grayscale image with inverted blurred image
pencil_sketch = cv2.divide(gray_image, inverted_blurred_img, scale = 256.0)
cv2.imshow('Pencil Sketch', pencil_sketch)
cv2.waitKey(0)