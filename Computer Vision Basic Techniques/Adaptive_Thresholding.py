import cv2
import numpy as np

image_read = cv2.imread("Computer Vision Basic Techniques\Images\Sample.png", cv2.IMREAD_GRAYSCALE)

threshold_value = 127

binary_image = cv2.adaptiveThreshold(image_read,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


cv2.imshow("BINARY_IMAGE", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()