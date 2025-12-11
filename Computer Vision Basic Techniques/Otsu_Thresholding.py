import cv2
import numpy as np

image_read = cv2.imread("Computer Vision Basic Techniques\Images\Sample.png", cv2.IMREAD_GRAYSCALE)

threshold_value = 0

_,binary_image = cv2.threshold(image_read, threshold_value, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow("BINARY_IMAGE", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()