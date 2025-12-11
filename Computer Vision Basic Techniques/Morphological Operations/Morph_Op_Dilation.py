import cv2
import numpy as np

image_read = cv2.imread("Computer Vision Basic Techniques\Images\Sample.png", cv2.IMREAD_GRAYSCALE)


kernel = np.ones((5,5), np.uint8)


dilated_image = cv2.dilate(image_read, kernel, iterations=1)

cv2.imshow("Dilated Image", dilated_image)


cv2.waitKey(0)
cv2.destroyAllWindows()