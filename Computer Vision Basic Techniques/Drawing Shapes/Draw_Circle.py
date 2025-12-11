import cv2
import numpy as np


image_read = np.zeros((500,500,3), dtype="uint8")

center_x, center_y = 250, 250
radius = 200
cv2.circle(image_read, (center_x, center_y), radius, color=(255,0,0), thickness=-2)

# cv2.circle(image_read, (center_x, center_y), radius, color=(255,0,0), thickness=(5))
cv2.imshow("DRAWN CIRCLE", image_read)
cv2.waitKey(0)
cv2.destroyAllWindows()