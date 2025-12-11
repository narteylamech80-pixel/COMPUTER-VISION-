import os
import cv2
from PIL import Image
import numpy as np

if not os.path.exists("Computer Vision Basic Techniques/Mask Image Generations/masks"):
    os.mkdir("Computer Vision Basic Techniques/Mask Image Generations/masks")
if not os.path.exists("Computer Vision Basic Techniques/Mask Image Generations/masks/normal"):
    os.mkdir("Computer Vision Basic Techniques/Mask Image Generations/masks/normal")
    
    
    #Creating normal mask images from annotation
for root, dirs, files in os.walk(r'C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Computer Vision Basic Techniques\Images\Gastric_image\normal'):
    for filename in files:
        print(filename)
        img = np.asarray(Image.open(r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Computer Vision Basic Techniques\Images\Gastric_image\normal/" + filename))
        print(img)
        img4 = np.zeros((img.shape[0],img.shape[1]))
        print(img4.shape)
        cv2.imwrite(r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Computer Vision Basic Techniques\Mask Image Generations\masks\normal/{}".format(filename),img4)