# import cv2
# image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_COLOR)
# cv2.imwrite("Computer Vision Basic Techniques/Output/output_image.png", image_read)



# import cv2
# image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_GRAYSCALE)
# cv2.imwrite("Computer Vision Basic Techniques/Output/output_image_grayscale.png", image_read)


# import cv2
# import numpy as np
# image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_GRAYSCALE)
# print(image_read.shape)
# grayscale_image_channel=np.expand_dims(image_read, axis=2)
# print(grayscale_image_channel.shape)
# cv2.imwrite("Computer Vision Basic Techniques/Output/Enhanced_output_image_grayscale_channel.png", grayscale_image_channel)



# import cv2
# import numpy as np
# image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_COLOR)
# print(image_read.shape)
# cv2.imwrite("Computer Vision Basic Techniques/Output/JPEG_output_IMAGE.png", image_read, [cv2.IMWRITE_JPEG_QUALITY, 90])



# import cv2
# import numpy as np
# image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_COLOR)
# print(image_read.shape)
# cv2.imwrite("Computer Vision Basic Techniques/Output/PNG_output_IMAGE.png", image_read, [cv2.IMWRITE_PNG_COMPRESSION,7])




# import cv2
# import numpy as np
# image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_COLOR)
# b,g,r= cv2.split(image_read)
# cv2.imwrite("Computer Vision Basic Techniques/Output/B_output_IMAGE.png", b)
# cv2.imwrite("Computer Vision Basic Techniques/Output/G_output_IMAGE.png", g)
# cv2.imwrite("Computer Vision Basic Techniques/Output/R_output_IMAGE.png", r)
# cv2.imwrite("Computer Vision Basic Techniques/Output/MergedBGR_output_IMAGE.png", cv2.merge((b,g,r)))



# import cv2
# import numpy as np
# image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_COLOR)
# print(image_read.shape)
# resized_image= cv2.resize(image_read, (128,128))
# print(resized_image.shape)
# cv2.imwrite("Computer Vision Basic Techniques/Output/Resized_output_IMAGE.png", resized_image)



# import cv2
# import numpy as np
# image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_COLOR)
# rgb_image= cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
# print(rgb_image.shape)
# cv2.imwrite("Computer Vision Basic Techniques/Output/RGB_output_IMAGE.png", rgb_image)




# import cv2
# import numpy as np
# image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", cv2.IMREAD_COLOR)
# hsv_image= cv2.cvtColor(image_read, cv2.COLOR_BGR2HSV)
# print(hsv_image.shape)
# cv2.imwrite("Computer Vision Basic Techniques/Output/HSV_output_IMAGE.png", hsv_image)





import cv2
import numpy as np

image_read= cv2.imread("Computer Vision Basic Techniques/Images/Sample.png", 0)
image_read= cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray to BGR", image_read)
cv2.waitKey(0)
cv2.destroyAllWindows()