import cv2
import queue
import threading
import time
from utils import get_default_camera


camera_index = get_default_camera()

pTime = 0
cTime = 0

def computation():
    time.sleep(0.5)


# bufferless VideoCapture
class VideoCapture:

  def __init__(self, name):
    self.cap = cv2.VideoCapture(name)
    self.q = queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # read frames as soon as they are available, keeping only most recent one
  def _reader(self):
    while True:
      ret, frame = self.cap.read()
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()   # discard previous (unprocessed) frame
        except queue.Empty:
          pass
      self.q.put(frame)

  def read(self):
    return self.q.get()

cap = VideoCapture(camera_index)
# cap = cv2.VideoCapture(camera_index)

while True:
    img = cap.read()

    # success, img = cap.read()

    computation()

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 5)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
        break # Esc
