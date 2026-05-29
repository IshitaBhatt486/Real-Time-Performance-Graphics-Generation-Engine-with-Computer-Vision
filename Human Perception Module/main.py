import time
import cv2

from camera.camera import Camera
from preprocessing.preprocessing import preprocessor
from humanDetection.humanDetector import HumanDetector
from tracking.temporalTracker import TemporalTracker
from tracking.identityTracker import IdentityTracker

camera = Camera()
preprocessor = preprocessor()
humanDetector = HumanDetector()
tracker = TemporalTracker()
identity_tracker = IdentityTracker()

while True:

    data = camera.get_frame()
    frame = data["frame"]
    fps = data["fps"]

    if frame is None:
        break

    timestamp_ms = int(
        time.time() * 1000
    )

    processed_frame = preprocessor.pre_process(frame)
    results = humanDetector.detect_human(processed_frame,timestamp_ms)

    people_pose_data = humanDetector.extract_landmarks(results, processed_frame.shape)

    if len(people_pose_data) == 0:
        continue

    pose_data = people_pose_data[0]

    smoothed_pose = tracker.smoothing(
        pose_data
    )

    tracked_people = identity_tracker.update(people_pose_data)

    copy_frame = processed_frame.copy()
    draw_connections = humanDetector.draw_connections(copy_frame, smoothed_pose)
    draw_trails = humanDetector.draw_trails( draw_connections, tracker.history)
    output = identity_tracker.draw_ids(draw_trails, tracked_people)

    cv2.imshow(
        "Motion Intelligence Engine",
        output
    )

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()