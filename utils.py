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
