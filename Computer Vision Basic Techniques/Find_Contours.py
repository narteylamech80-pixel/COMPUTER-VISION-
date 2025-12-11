import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from IPython.display import Image





image_read = cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_COLOR)

gray_image = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)

_,binary_image = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)

kernels = np.ones((5,5),dtype=np.uint8)

contour_image, hierarchy =cv2.findContours(binary_image,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(contour_image)


# THE COMMENT SECTION BELOW DOESNT WORK WITH THIS CODE ABOVE

# cv2.imshow("IMAGE",contour_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

