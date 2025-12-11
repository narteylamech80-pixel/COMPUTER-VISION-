import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from IPython.display import Image




image_read = cv2.imread("Computer Vision Basic Techniques\Images\Sample.png", cv2.IMREAD_COLOR)

gray_image = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)

_,binary_image = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)

kernels = np.ones((5,5),dtype=np.uint8)

morph_image=cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernels)

plt.imshow(morph_image)

cv2.imshow("IMAGE",morph_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

