import time
import cv2

from camera.camera import Camera
from preprocessing.preprocessing import preprocessor
from humanDetection.humanDetector import HumanDetector

camera = Camera()
preprocessor = preprocessor()
humanDetector = HumanDetector()

while True:

    data = camera.get_frame()

    frame=data["frame"]
    fps=data["fps"]

    timestamp_ms = int(time.time() * 1000)

    if frame is None:
        break

    results = humanDetector.detect_human(
        frame,
        timestamp_ms
    )

    output = humanDetector.draw_landmarks(
        frame,
        results
    )

    cv2.imshow(
        "Human Detection",
        output
    )

    if cv2.waitKey(1)==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()