import cv2
import numpy as np


image_read = np.zeros((500,500,3), dtype="uint8")

start_x, start_y = 100, 400
end_x, end_y = 400, 100 

cv2.rectangle(image_read, pt1=(start_x,start_y), pt2=(end_x,end_y),color=(255,0,0), thickness=(5))
cv2.imshow("DRAWN RECT", image_read)
cv2.waitKey(0)
cv2.destroyAllWindows()