import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("NO CAMERA DETECTED")
    exit()
    
while True:
    ret, frame= cap.read()
     
    if not ret:
        print("NO CAMERA DETECTED")
        break
    
    cv2.imshow("Video Display", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
       
cap.release()
cv2.destroyAllWindows()