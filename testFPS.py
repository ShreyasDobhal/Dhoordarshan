
import cv2
import time
import numpy as np
from utils import get_default_camera


camera_index = get_default_camera()

cap = cv2.VideoCapture(camera_index)

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break # Esc

cap.release()
cv2.destroyAllWindows()