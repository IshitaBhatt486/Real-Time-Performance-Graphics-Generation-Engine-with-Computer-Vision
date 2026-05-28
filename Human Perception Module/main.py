import cv2
import numpy as np

from camera.camera import Camera
from preprocessing.preprocessing import preprocessor

camera = Camera()
preprocessor = preprocessor()

while True:

    data = camera.get_frame()

    frame=data["frame"]
    fps=data["fps"]

    if frame is None:
        break

    processed_frame = preprocessor.pre_process(frame)

    display = (processed_frame * 255).astype(np.uint8)

    cv2.imshow("Processed frame", display)

    if cv2.waitKey(1)==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()