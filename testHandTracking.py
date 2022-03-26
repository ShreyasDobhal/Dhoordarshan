from handTrackingModule import handDetector

import cv2
import time
from handTrackingModule import handDetector
import numpy as np
from utils import get_default_camera


camera_index = get_default_camera()

cap = cv2.VideoCapture(camera_index)
detector = handDetector(max_hands=1)

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    fingers = detector.getFingerState(landmark_list=lmList)
    if fingers:
        print(fingers)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break # Esc

cap.release()
cv2.destroyAllWindows()