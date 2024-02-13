import cv2
import time
from invoke_ps1 import invoke_lock_script
# Load pre-trained face and eye detection models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def detect_eyes(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print("----------------")
    print("face", faces)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # Detect eyes within the region of interest (ROI)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        print("eye", eyes)
        print("eye tensor len" , len(eyes))
        print("--------------")
        if len(eyes) == 0:
            return True  # Eyes closed
    if len(faces) == 0:
        return True
    else:    
        return False  # Eyes open


def main():
    video_capture = cv2.VideoCapture(0)  # Use default camera
    
    while True:
        ret, frame = video_capture.read()
        # print(ret , frame)
        if not ret:
            break

        # Detect eyes
        if detect_eyes(frame):
            # Eyes closed or face not detected
            # Lock the laptop here (you need to implement this part)
            print("Locking the laptop...")
            invoke_lock_script()

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(10000) & 0xFF == ord('q'):  # Check every 5 seconds
            break

    # Release the camera and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
