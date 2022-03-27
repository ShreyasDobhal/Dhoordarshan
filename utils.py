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
    return 2

def get_name():
    return 'Home'

def get_googlemeet_url():
    return 'https://meet.google.com/fhd-daqi-ddm'

def get_facetime_url():
    return 'https://facetime.apple.com/join#v=1&p=CWu/6a2oEeyI8wJC3qtUKg&k=QKBOGNnEbvIV37XqLsiQH4cJLIAxnztVomOCm-20B6E'

def get_steps(key):
    step_map = {
        'facetime': [
            # Wait to connect
            ['delay', 10],
            # Open URL
            ['open', get_facetime_url()],
            ['delay', 2],
            # Enter name
            ['jump', (900, 620)],
            ['click', 'left'],
            ['type', get_name()],
            # Click continue
            ['jump', (900, 685)],
            ['click', 'left'],
            # Wait to connect
            ['delay', 10],
            # Click join
            ['jump', (410, 980)],
            ['click', 'left']
        ],
        'googlemeet': [
            # Wait to connect
            ['delay', 10],
            # Open URL
            ['open', get_googlemeet_url()],
            ['delay', 2],
            # Enter name
            ['jump', (1300, 550)],
            ['click', 'left'],
            ['type', get_name()],
            # Ask to join
            ['jump', (1300, 625)],
            ['click', 'left'],
            # # Wait to connect
            ['delay', 10],
            # # Click join
            # ['jump', (410, 980)],
            # ['click', 'left']
        ]
    }

    return step_map[key]