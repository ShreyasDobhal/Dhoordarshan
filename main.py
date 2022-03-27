import cv2
import time
import pyfakewebcam
from handTrackingModule import handDetector
import numpy as np
from utils import get_default_camera, get_facetime_url, get_steps
from FastCapture import VideoCapture
import threading
from followSteps import perform_steps, open_page

preview = True
width = 640
height = 480

camera_index = get_default_camera()

print('Camera:', camera_index)
if camera_index is None:
    print('No camera found')
    exit()

# cap = cv2.VideoCapture(camera_index)
cap = VideoCapture(camera_index)
detector = handDetector(max_hands=1)

pTime = 0
cTime = 0

loading = 0
doneLoading = False
coolDownThreshold = 3
coolDown = 0

fake = pyfakewebcam.FakeWebcam('/dev/video20', width, height)

def detect_gesture_and_stream_camera():
    global cap, detector, pTime, cTime, loading, doneLoading, coolDownThreshold, coolDown
    global preview, width, height, camera_index, fake
    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw=doneLoading)
        lmList = detector.findPosition(img, draw=False)

        if lmList:
            id, cx, cy = lmList[-1]
            if not doneLoading:
                cv2.ellipse(img, (cx, cy), (50, 50), -90, 0, loading / 100 * 360, (255, 0, 0), 5, cv2.LINE_AA)

                loading += 4
                if loading >= 100:
                    loading = 100
                    doneLoading = True
            coolDown = 0
        else:
            cTime = time.time()
            if coolDown == 0:
                coolDown = cTime
            
            if cTime - coolDown > coolDownThreshold:
                loading = 0
                doneLoading = False
        
        if doneLoading:
            # Identifying finger state
            fingers = detector.getFingerState(landmark_list=lmList)
            if fingers:
                print(fingers)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

        if preview:
            cv2.imshow("Image", img)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fake.schedule_frame(img)

        if cv2.waitKey(1) == 27:
            break # Esc

    cv2.destroyAllWindows()
    exit()


# Start camera in separate thread
camera_thread = threading.Thread(target=detect_gesture_and_stream_camera)
camera_thread.start()

# Start performing the steps
# print('Starting . . .')
# perform_steps(get_steps('googlemeet'))