import cv2
import time
from utils import get_default_camera
from FastCapture import VideoCapture

camera_index = get_default_camera()

pTime = 0
cTime = 0

def computation():
    time.sleep(0.5)

cap = VideoCapture(camera_index)

while True:
    success, img = cap.read()

    computation()

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
        break # Esc
