import cv2
import numpy as np

image_read = cv2.imread("Computer Vision Basic Techniques\Images\Sample.png", cv2.IMREAD_GRAYSCALE)

_,binary_image = cv2.threshold(image_read, 127, 255, cv2.THRESH_BINARY)


kernel = np.ones((5,5), np.uint8)


eroded_image = cv2.erode(binary_image, kernel, iterations=1)

cv2.imshow("Eroded Image", eroded_image)


cv2.waitKey(0)
cv2.destroyAllWindows()