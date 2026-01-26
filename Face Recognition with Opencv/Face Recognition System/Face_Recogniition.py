import cv2
import pandas as pd
import face_recognition
import os



def load_data_from_folder (folder, metadata_file):
    images = []
    labels = []
    metadata = []
    
    metadata_df = pd.read_excel(metadata_file)
    metadata_dict = metadata_df.set_index("Unique Identifier").T.to_dict("list")
    
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = face_recognition.load_image_file(os.path.join(folder, filename))
            encodings = face_recognition.face_encodings(img)
            if len(encodings) == 0:
                continue
            images.append(encodings[0])
            # images.append(encodings)
            labels.append(filename.split(".")[0])
            identifier = filename.split(".")[0]
            if identifier in metadata_dict :
                metadata.append(metadata_dict[identifier])
            else:
                metadata.append(["Unknown", "Unknown", "Unknown"])
                
    return images, labels, metadata

training_data_folder = r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\Sample Data"
metadata_file = r"C:\Users\Charles Nartey\OneDrive\Desktop\CV\Computer Vision\Face Recognition with Opencv\9 - TrainingDataNameAgeGender.xlsx"

known_face_encodings, known_face_names, metadata = load_data_from_folder(training_data_folder, metadata_file)

video_capture = cv2.VideoCapture(0)
while True:
     ret, frame = video_capture.read()
     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
     face_locations = face_recognition.face_locations(rgb_frame)
     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

     
     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            name = "Unknown"
            fullname = "Unknown"
            age = "Unknown"
            gender = "Unknown"
            color = (0, 0, 255)  # red = denied

            if len(face_distances) > 0:
                    best_match_index = face_distances.argmin()

                    if face_distances[best_match_index] < 0.40:
                        name = known_face_names[best_match_index]
                        fullname, gender, age = metadata[best_match_index]
                        color = (0, 255, 0)

                        cv2.putText(frame, "Identity Verified, Access Granted",(50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
                    else:
                        cv2.putText(frame, "Identity Not Verified, Access Denied",(50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)

                    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                    cv2.putText(frame, f"Name: {fullname}", (left, bottom + 20),cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)
                    cv2.putText(frame, f"Age: {age}", (left, bottom + 40),cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)
                    cv2.putText(frame, f"Gender: {gender}", (left, bottom + 60),cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)

     
     cv2.imshow("VIDEO",frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

            
            
                         