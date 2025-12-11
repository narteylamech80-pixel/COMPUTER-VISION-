import cv2
import numpy as np


image_read = np.zeros((500,500,3), dtype="uint8")

start_x, start_y = 0, 250
end_x, end_y = 500, 250

cv2.line(image_read, pt1=(start_x,start_y), pt2=(end_x,end_y),color=(255,0,0), thickness=(5))
cv2.imshow("DRAWN LINE", image_read)
cv2.waitKey(0)
cv2.destroyAllWindows()