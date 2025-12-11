import cv2
import numpy as np


image_read= cv2.imread("Computer Vision Basic Techniques\Images\Sample.png", cv2.IMREAD_COLOR)

x1=500; x2=400;
y1=500; y2=400;

cropped_image= image_read[y2:y1, x2:x1]
cv2.imshow("CROPPED IMAGE", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
