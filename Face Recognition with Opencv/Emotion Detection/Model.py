import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.utils import to_categorical


emotion_folders = [
    r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Emotions Dataset\train\angry",
    r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Emotions Dataset\train\surprise",
    r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Emotions Dataset\train\disgust",
    r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Emotions Dataset\train\fear",
    r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Emotions Dataset\train\happy",
    r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Emotions Dataset\train\neutral",
    r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Emotions Dataset\train\sad"
]

def load_data(emotion_folders):
    images = []
    labels = []
    
    for i, folder in enumerate(emotion_folders):
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (48,48))
            images.append(img)
            labels.append(i)
    return np.array(images), np.array(labels)

images, labels = load_data(emotion_folders)

x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
x_train = x_train.reshape(x_train.shape[0], 48, 48, 1).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 48, 48, 1).astype('float32') / 255

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape =(48,48,1)))
model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))

model.compile(loss="categorical_crossentropy", optimizer='adam', metrics=["accuracy"])
model.fit(x_train, y_train, batch_size=64, epochs=20, verbose=1, validation_data=(x_test, y_test))

model.save("Epitome_Emotion_Detection_Model.keras")