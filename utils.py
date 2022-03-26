import cv2

def get_camera_indexes():
    index = 0
    camera_indexes = []
    i = 5
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            camera_indexes.append(index)
            cap.release()
        index += 1
        i -= 1
    return camera_indexes

def math_dist(point1, point2):
    return (point1[0]-point2[0])*(point1[0]-point2[0]) + (point1[1]-point2[1])*(point1[1]-point2[1])

def get_default_camera():
    return 0

def get_meeting_id():
    return 'muz-nktg-pbt'