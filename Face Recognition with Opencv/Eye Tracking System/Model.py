import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.utils import to_categorical


left_eye_folder = r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Eye Dataset\left_look"
right_eye_folder = r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Eye Dataset\right_look"


def load_data(folder):
    images = []
    labels = []
    
    for filename in os.listdir(folder):        
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (48,48))
            images.append(img)
            label = 0 if folder.endswith("left_look") else 1
            labels.append(label)
    return np.array(images), np.array(labels)

images_left, labels_left = load_data(left_eye_folder)
images_right, labels_right = load_data(right_eye_folder)


images_combine = np.concatenate((images_left, images_right), axis = 0 )
labels_combine = np.concatenate((labels_left, labels_right), axis = 0)

images_normalized = images_combine.reshape(-1, 48, 48, 1).astype('float32')/255
labels_binary = to_categorical(labels_combine)

x_train, x_test, y_train, y_test = train_test_split(images_normalized, labels_binary, test_size=0.2, random_state=42)


model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape =(48,48,1)))
model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

model.compile(loss="categorical_crossentropy", optimizer='adam', metrics=["accuracy"])
model.fit(x_train, y_train, batch_size=64, epochs=20, verbose=1, validation_data=(x_test, y_test))

model.save("Epitome_Eye_Tracking_Model.keras")