import time
import cv2

from camera.camera import Camera
from preprocessing.preprocessing import preprocessor
from humanDetection.humanDetector import HumanDetector
from tracking.temporalTracker import TemporalTracker

camera = Camera()
preprocessor = preprocessor()
humanDetector = HumanDetector()
tracker = TemporalTracker()

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

    pose_data = humanDetector.extract_landmarks(
        results,
        frame.shape
    )

    smoothed_pose = tracker.smoothing(
        pose_data
    )

    skeletal_frame = humanDetector.draw_connections(
        frame,
        smoothed_pose
    )

    output = humanDetector.draw_trails(
        skeletal_frame,
        tracker.history
    )

    cv2.imshow(
        "Human Detection",
        output
    )

    if cv2.waitKey(1)==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()