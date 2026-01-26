import cv2
from keras.models import load_model
import numpy as np


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

eye_model = load_model("Face Recognition with Opencv/Eye Tracking System/Epitome_Eye_Tracking_Model.keras")

threshold = 0.9


def detect_eye(eye_image):
    eye_image = cv2.resize(eye_image, (48, 48))
    eye_image = cv2.cvtColor(eye_image, cv2.COLOR_BGR2GRAY)

    eye_image = np.expand_dims(eye_image, axis=0)
    eye_image = np.expand_dims(eye_image, axis= -1)
    eye_image = eye_image.astype("float32")/255
    
    prediction = eye_model.predict(eye_image, verbose= 0)
    class_id = np.argmax(prediction)
    confidence = np.max(prediction)
    
    if confidence > threshold and class_id == 1:
        return True
    else:
        return False

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
    
#     for (x,y,w,h) in faces:
#         eye_region = frame[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(eye_region)
        
#         movement = detect_eye(eye_region)
        
#         if movement:
#             cv2.putText(frame, "Suspicious Behaviour Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
#         else:
#             cv2.putText(frame, "", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
                    
#     cv2.imshow("Eye Detection", frame)
    
#     if cv2.waitKey(1) & 0xff == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()


# ##############################################################################################################################
##########  AI ENHANCED CODE  #########################

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        face_roi_gray = gray[y:y+h, x:x+w]
        face_roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(face_roi_gray, 1.1, 5)

        for (ex, ey, ew, eh) in eyes:
            eye_img = face_roi_color[ey:ey+eh, ex:ex+ew]
            movement = detect_eye(eye_img)

            if movement:
                cv2.putText(
                    frame,
                    "Suspicious Eye Movement",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

            cv2.rectangle(
                face_roi_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (0, 255, 0),
                2
            )

    cv2.imshow("Eye Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
