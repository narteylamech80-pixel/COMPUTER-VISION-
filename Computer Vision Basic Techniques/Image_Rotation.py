import cv2
import numpy as np

image_read= cv2.imread("Computer Vision Basic Techniques\Images\Sample.png", cv2.IMREAD_COLOR)
h, w, c = image_read.shape

center = (h//2, w//2)
angle = 45
m = cv2.getRotationMatrix2D(center, angle, 1.0)

rotated_image = cv2.warpAffine(image_read,m,(w,h))

cv2.imshow("Rotated Image",rotated_image)
cv2.waitKey(0)