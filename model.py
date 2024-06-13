import cv2
import os

img = cv2.imread(r"C:\Users\HP\Documents\CodeClause\Image to Sketch\ArcticMonkeys.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255 - gray_image

blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
inverted_blurred_image = 255 - blurred_image
pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

cv2.imshow('Original Image', img)
cv2.imshow('Pencil Sketch Image', pencil_sketch_image)
cv2.waitKey(0)
cv2.destroyAllWindows()