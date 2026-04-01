# import tkinter as tk
# from tkinter import messagebox
# import cv2
# import time
# import numpy as np
# from PIL import Image, ImageTk
# from datetime import datetime
# import pickle
# import json
# import os
# from tinydb import TinyDB, where
# import face_recognition
# from project.utils import Conf

# # Initialize the configuration and recognizer
# # Resolve config path relative to this script's location
# script_dir = os.path.dirname(os.path.abspath(__file__))
# config_file = os.path.join(script_dir, "config", "config.json")
# conf = Conf(config_file)

# # Resolve paths relative to script directory; try workspace-level output as a fallback
# workspace_root = os.path.dirname(script_dir)

# def resolve_path_try_workspace(relpath):
#     # normalize separator and handle absolute paths
#     p = relpath.replace('/', os.sep)
#     if os.path.isabs(p):
#         return os.path.normpath(p)
#     # candidates: script_dir first, then workspace_root
#     cand_script = os.path.normpath(os.path.join(script_dir, p))
#     cand_workspace = os.path.normpath(os.path.join(workspace_root, p))
#     if os.path.exists(cand_script):
#         return cand_script
#     if os.path.exists(cand_workspace):
#         return cand_workspace
#     # fallback to script candidate
#     return cand_script

# # Recognizer
# recognizer_path = resolve_path_try_workspace(conf["recognizer_path"])
# if not os.path.exists(recognizer_path):
#     print(f"Error: recognizer not found at {recognizer_path}")
#     print("Expected recognizer.pickle in either app 'output' or workspace 'output' folder. Run encoder first.")
#     import sys
#     sys.exit(1)
# recognizer = pickle.loads(open(recognizer_path, "rb").read())

# # Label encoder
# le_path = resolve_path_try_workspace(conf["le_path"])
# if not os.path.exists(le_path):
#     print(f"Error: label encoder not found at {le_path}")
#     print("Expected le.pickle in either app 'output' or workspace 'output' folder. Run encoder first.")
#     import sys
#     sys.exit(1)
# le = pickle.loads(open(le_path, "rb").read())

# # Initialize the TinyDB for attendance and students
# db_path = conf["db_path"]
# if not os.path.isabs(db_path):
#     db_path = os.path.join(script_dir, db_path)
# db = TinyDB(db_path)
# studentTable = db.table("student")
# json_file_path_enroll = os.path.join(script_dir, "database", "enroll.json")
# json_file_path_attendance = os.path.join(script_dir, "attendance.json")

# # Helper: safely find a student's name by their ID in the TinyDB student table
# def get_student_name(student_id):
#     """
#     student_id: string id used as the key in student records (enroll.py inserts {id: [name, status]})
#     Returns the stored name string or None if not found.
#     """
#     try:
#         for rec in studentTable.all():
#             # each rec is expected to be a dict like {"123": ["Alice", "enrolled"]}
#             if student_id in rec:
#                 value = rec[student_id]
#                 if isinstance(value, (list, tuple)) and len(value) > 0:
#                     return value[0]
#                 # if stored as dict or string, try to handle common shapes
#                 if isinstance(value, dict):
#                     return value.get("name") or value.get("student_name")
#                 if isinstance(value, str):
#                     return value
#     except Exception:
#         # If the DB is in an unexpected state, fall back gracefully
#         return None
#     return None

# # Initialize the video capture
# vs = cv2.VideoCapture(0, cv2.CAP_MSMF)
# # Function to store attendance
# def store_attendance(name, id):
#     if not name or name.lower() == "unknown":
#         print("Face not recognized, attendance not stored.")
#         return

#     try:
#         with open(json_file_path_enroll, 'r') as file:
#             enroll_data = json.load(file)
#     except FileNotFoundError:
#         enroll_data = {"_default": {}, "student": {}}

#     students = enroll_data.get("student", {})
#     try:
#         with open(json_file_path_attendance, 'r') as file:
#             attendance_data = json.load(file)
#     except FileNotFoundError:
#         attendance_data = {"attendance": {}}

#     current_date = datetime.now().strftime("%Y-%m-%d")

#     if id in attendance_data['attendance']:
#         attendance_date = attendance_data['attendance'][id].get('date_time', "").split(" ")[0]
#         if attendance_date == current_date:
#             return f"Attendance for {name} (ID: {id}) already recorded for today."

#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     attendance_data['attendance'][id] = {
#         "name": name,
#         "date_time": current_time
#     }

#     print(f"Stored attendance for {name} (ID: {id}) at {current_time}")

#     with open(json_file_path_attendance, 'w') as file:
#         json.dump(attendance_data, file, indent=4)

# # Tkinter window setup
# root = tk.Tk()
# root.title("Smart Face Attendance System")
# root.geometry("800x600")

# # Label to show attendance status
# attendance_label = tk.Label(root, text="Attendance Recognition: ", font=("Arial", 16))
# attendance_label.pack(pady=20)

# # Canvas to display video feed
# canvas = tk.Canvas(root, width=640, height=480)
# canvas.pack()

# # Initialize variables
# prevPerson = None
# curPerson = None
# consecCount = 0
# video_running = False  # Flag to check if the video feed is running

# # Function to update the GUI with the video feed and attendance status
# def update_frame():
#     global prevPerson, curPerson, consecCount, video_running

#     if not video_running:
#         return  # Stop updating frames if video is not running

#     ret, frame = vs.read()
#     if not ret:
#         print("Failed to grab frame")
#         return

#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     gray_image = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
#     gray_img = np.expand_dims(gray_image, axis=2).repeat(3, axis=2)

#     boxes = face_recognition.face_locations(gray_img, model=conf["detection_method"])

#     for (top, right, bottom, left) in boxes:
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#     if len(boxes) > 0:
#         encodings = face_recognition.face_encodings(rgb, boxes)
#         preds = recognizer.predict_proba(encodings)[0]
#         j = np.argmax(preds)
#         confidence = preds[j]
        
#         print("Prediction probabilities:", preds)
#         print("Best match:", le.classes_[j])
#         print("Confidence:", preds[j])

#         confidence_threshold = 0.75
#         if confidence < confidence_threshold:
#             curPerson = "Unknown"
#             return
#         curPerson = le.classes_[j]

#         if prevPerson == curPerson:
#             consecCount += 1
#         else:
#             consecCount = 0

#         prevPerson = curPerson

#         # Safe lookup: previous code assumed search would always return a matching document
#         # which raised IndexError when student record wasn't present. Use the helper instead.
#         name = get_student_name(curPerson)
#         if not name:
#             name = "Unknown"
#         cv2.putText(frame, "Status:Face Detecting", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#         attn_info = store_attendance(name, curPerson)
#         if attn_info:
#             attendance_label.config(text=f"Attendance Status: {attn_info}")
#         else:
#             attendance_label.config(text=f"Attendance Status: {name}")

#     # Convert the frame to an ImageTk object and update the canvas
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     img = Image.fromarray(frame_rgb)
#     img_tk = ImageTk.PhotoImage(image=img)

#     canvas.create_image(0, 0, anchor="nw", image=img_tk)
#     canvas.image = img_tk

#     # Repeat the frame update every 10 milliseconds
#     root.after(10, update_frame)

# # Start button function
# def start_video():
#     global video_running
#     video_running = True
#     update_frame()

# # Exit button function
# def exit_program():
#     global video_running
#     video_running = False  # Stop the video feed
#     vs.release()  # Release the video capture
#     cv2.destroyAllWindows()  # Close all OpenCV windows
#     root.quit()  # Exit the Tkinter main loop

# # Start button setup
# start_button = tk.Button(root, text="Start", font=("Arial", 16), bg="#00ff00", command=start_video)
# start_button.pack(pady=10)

# # Exit button setup
# exit_button = tk.Button(root, text="Exit", font=("Arial", 16), bg="#ff0000", command=exit_program)
# exit_button.pack(pady=20)

# # Start the Tkinter main loop
# root.mainloop()

# # Clean up after exiting the Tkinter window
# vs.release()
# cv2.destroyAllWindows()



import tkinter as tk
from tkinter import messagebox
import cv2
import time
import numpy as np
from PIL import Image, ImageTk
from datetime import datetime
import pickle
import json
import os
from tinydb import TinyDB, where
import face_recognition
from project.utils import Conf

# Initialize the configuration and recognizer
script_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(script_dir, "config", "config.json")
conf = Conf(config_file)

workspace_root = os.path.dirname(script_dir)

def resolve_path_try_workspace(relpath):
    p = relpath.replace('/', os.sep)
    if os.path.isabs(p):
        return os.path.normpath(p)
    cand_script = os.path.normpath(os.path.join(script_dir, p))
    cand_workspace = os.path.normpath(os.path.join(workspace_root, p))
    if os.path.exists(cand_script):
        return cand_script
    if os.path.exists(cand_workspace):
        return cand_workspace
    return cand_script

# Recognizer
recognizer_path = resolve_path_try_workspace(conf["recognizer_path"])
if not os.path.exists(recognizer_path):
    print(f"Error: recognizer not found at {recognizer_path}")
    import sys
    sys.exit(1)
recognizer = pickle.loads(open(recognizer_path, "rb").read())

# Label encoder
le_path = resolve_path_try_workspace(conf["le_path"])
if not os.path.exists(le_path):
    print(f"Error: label encoder not found at {le_path}")
    import sys
    sys.exit(1)
le = pickle.loads(open(le_path, "rb").read())

# Initialize TinyDB
db_path = conf["db_path"]
if not os.path.isabs(db_path):
    db_path = os.path.join(script_dir, db_path)
db = TinyDB(db_path)
studentTable = db.table("student")
json_file_path_enroll = os.path.join(script_dir, "database", "enroll.json")
json_file_path_attendance = os.path.join(script_dir, "attendance.json")

# Helper: safely find student name
def get_student_name(student_id):
    try:
        for rec in studentTable.all():
            if student_id in rec:
                value = rec[student_id]
                if isinstance(value, (list, tuple)) and len(value) > 0:
                    return value[0]
                if isinstance(value, dict):
                    return value.get("name") or value.get("student_name")
                if isinstance(value, str):
                    return value
    except Exception:
        return None
    return None

# Initialize video capture
vs = cv2.VideoCapture(0, cv2.CAP_MSMF)

# Function to store attendance
def store_attendance(name, id):
    if not name:
        print("Face not recognized, attendance not stored.")
        return

    try:
        with open(json_file_path_enroll, 'r') as file:
            enroll_data = json.load(file)
    except FileNotFoundError:
        enroll_data = {"_default": {}, "student": {}}

    students = enroll_data.get("student", {})
    try:
        with open(json_file_path_attendance, 'r') as file:
            attendance_data = json.load(file)
    except FileNotFoundError:
        attendance_data = {"attendance": {}}

    current_date = datetime.now().strftime("%Y-%m-%d")

    if id in attendance_data['attendance']:
        attendance_date = attendance_data['attendance'][id].get('date_time', "").split(" ")[0]
        if attendance_date == current_date:
            return f"Attendance for {name} (ID: {id}) already recorded for today."

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    attendance_data['attendance'][id] = {
        "name": name,
        "date_time": current_time
    }

    print(f"Stored attendance for {name} (ID: {id}) at {current_time}")

    with open(json_file_path_attendance, 'w') as file:
        json.dump(attendance_data, file, indent=4)

# Tkinter setup
root = tk.Tk()
root.title("Smart Face Attendance System")
root.geometry("800x600")

attendance_label = tk.Label(root, text="Attendance Recognition: ", font=("Arial", 16))
attendance_label.pack(pady=20)

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

prevPerson = None
curPerson = None
consecCount = 0
video_running = False

# Confidence threshold
CONFIDENCE_THRESHOLD = 0.75

def update_frame():
    global prevPerson, curPerson, consecCount, video_running

    if not video_running:
        return

    ret, frame = vs.read()
    if not ret:
        print("Failed to grab frame")
        return

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    gray_img = np.expand_dims(gray_image, axis=2).repeat(3, axis=2)

    boxes = face_recognition.face_locations(gray_img, model=conf["detection_method"])

    for (top, right, bottom, left) in boxes:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    if len(boxes) > 0:
        encodings = face_recognition.face_encodings(rgb, boxes)
        preds = recognizer.predict_proba(encodings)[0]
        j = np.argmax(preds)
        confidence = preds[j]

        # Apply confidence threshold
        if confidence < CONFIDENCE_THRESHOLD:
            curPerson = "Unknown"
            print("Confidence too low, face not recognized.")
        else:
            curPerson = le.classes_[j]

        if prevPerson == curPerson:
            consecCount += 1
        else:
            consecCount = 0
        prevPerson = curPerson

        name = get_student_name(curPerson)
        if not name and curPerson != "Unknown":
            print(f"Student ID {curPerson} not found in database.")
            name = curPerson  # fallback to ID

        if curPerson != "Unknown":
            attn_info = store_attendance(name, curPerson)
            if attn_info:
                attendance_label.config(text=f"Attendance Status: {attn_info}")
            else:
                attendance_label.config(text=f"Attendance Status: {name}")
        else:
            attendance_label.config(text="Attendance Status: Unknown")

        # Draw text on video
        status_text = f"{name} ({confidence*100:.1f}%)" if curPerson != "Unknown" else "Unknown"
        cv2.putText(frame, status_text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    img_tk = ImageTk.PhotoImage(image=img)

    canvas.create_image(0, 0, anchor="nw", image=img_tk)
    canvas.image = img_tk

    root.after(10, update_frame)

def start_video():
    global video_running
    video_running = True
    update_frame()

def exit_program():
    global video_running
    video_running = False
    vs.release()
    cv2.destroyAllWindows()
    root.quit()

start_button = tk.Button(root, text="Start", font=("Arial", 16), bg="#00ff00", command=start_video)
start_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 16), bg="#ff0000", command=exit_program)
exit_button.pack(pady=20)

root.mainloop()

vs.release()
cv2.destroyAllWindows()
