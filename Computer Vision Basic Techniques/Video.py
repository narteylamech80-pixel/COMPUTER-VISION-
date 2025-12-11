import cv2

cap = cv2.VideoCapture("Computer Vision Basic Techniques/Videos/SampleVideo.mp4")

if not cap.isOpened():
    print("Error in opening video file")
    exit()
    
while True:
    ret, frame= cap.read()
     
    if not ret:
        print("End of video file reached")
        break
    
    cv2.imshow("Video Display", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
       
cap.release()
cv2.destroyAllWindows()


