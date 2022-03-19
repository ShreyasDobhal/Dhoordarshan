import cv2
import time
import pyvirtualcam
from handTrackingModule import handDetector
import numpy as np
from utils import get_camera_indexes

preview = True

# camera_options = get_camera_indexes()
camera_options = [2]
print('Camera:', camera_options)
if len(camera_options) == 0:
    print('No camera found')
    exit()

camera_index = camera_options[-1]
cap = cv2.VideoCapture(camera_index)
detector = handDetector(max_hands=1)

pTime = 0
cTime = 0

loading = 0
doneLoading = False
coolDownThreshold = 3
coolDown = 0

fmt = pyvirtualcam.PixelFormat.BGR
# with pyvirtualcam.Camera(width=640, height=480, fps=20, device='/dev/video4') as cam:
with pyvirtualcam.Camera(width=640, height=480, fps=20, device='/dev/video4', fmt=fmt) as cam:
    print(f'Using virtual camera: {cam.device}')
    # frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB
    # while True:
    #     frame[:] = cam.frames_sent % 255  # grayscale animation
    #     cam.send(frame)
    #     cam.sleep_until_next_frame()


    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw=doneLoading)
        lmList = detector.findPosition(img, draw=False)
        fingers = detector.getFingerState(landmark_list=lmList)
        if fingers:
            print(fingers)

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

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

        if preview:
            cv2.imshow("Image", img)


        cam.send(img)
        cam.sleep_until_next_frame()

        if cv2.waitKey(1) == 27:
            break # Esc

    cv2.destroyAllWindows()