from email.mime import base
from gettext import find
import cv2
import mediapipe as mp
import time
import numpy as np
from utils import get_camera_indexes, math_dist

tip_indexes = [4, 8, 12, 16, 20]
palm_points = [0, 5, 9, 13, 17]

class handDetector():
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.track_confidence
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    
        return img
    
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]


            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            # Find the centroid
            
            cx = int(np.sum(list(map(lambda i: lmList[i][1], palm_points))) / len(palm_points))
            cy = int(np.sum(list(map(lambda i: lmList[i][2], palm_points))) / len(palm_points))
            lmList.append([21, cx, cy])

            if draw:
                cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        if len(lmList) == 0:
            return None
        return lmList

    def getFingerState(self, img=None, landmark_list=-1 , handNo=0):
        fingers = []

        if landmark_list == -1:
            landmark_list = self.findPosition(img, handNo, False)

        if landmark_list:
            # Thumb
            if landmark_list[tip_indexes[0]][1] > landmark_list[tip_indexes[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            
            # Fingers
            for id in range(1, 5):
                def get_point(id):
                    return landmark_list[id][1], landmark_list[id][2]
                tip_point = get_point(tip_indexes[id])
                base_point = get_point(tip_indexes[id] - 2)
                wrist_point = get_point(0)

                if math_dist(tip_point, wrist_point) > math_dist(base_point, wrist_point):
                    fingers.append(1)
                else:
                    fingers.append(0)

        if len(fingers) == 0:
            return None
        return fingers

        
                    

def main():
    camera_options = get_camera_indexes()
    print('Camera:', camera_options)
    if len(camera_options) == 0:
        print('No camera found')
        exit()

    camera_index = camera_options[-1]
    cap = cv2.VideoCapture(camera_index)
    detector = handDetector()

    pTime = 0
    cTime = 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if lmList:
            print(lmList[0])

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()