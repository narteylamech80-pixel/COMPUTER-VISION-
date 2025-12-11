import cv2
import numpy as np

# Create blank black image
image= np.ones((100, 100, 3), dtype=np.uint8)

# Define polygon points
points = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)

points = points.reshape((-1, 1, 2))

cv2.polylines(image, [points], isClosed=True, color=(0,255,255), thickness=2 )

cv2.imshow("POLYGON", image)
cv2.waitKey(0)
cv2.destroyAllWindows()