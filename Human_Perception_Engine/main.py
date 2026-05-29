import time
import cv2

from camera.camera import Camera
from preprocessing.preprocessing import preprocessor
from humanDetection.humanDetector import HumanDetector
from tracking.temporalTracker import TemporalTracker
from tracking.identityTracker import IdentityTracker
from segmentation.humanSegmentation import HumanSegmentation

camera = Camera()
preprocessor = preprocessor()
humanDetector = HumanDetector()
tracker = TemporalTracker()
identity_tracker = IdentityTracker()
segmentor = HumanSegmentation()

frame_counter = 0
cached_mask = None

while True:

    frame_counter += 1

    if frame_counter % 5 == 0:

        segmentation_map = segmentor.segment(
            processed_frame
        )

        person_mask = (
            segmentor.create_person_mask(
                segmentation_map
            )
        )

        smooth_mask = (
            segmentor.addGaussianBlur(
                person_mask
            )
        )

        cached_mask = smooth_mask

    if cached_mask is not None:

        isolated_human = (
            segmentor.extract_human(
                processed_frame,
                cached_mask
            )
        )

    data = camera.get_frame()
    frame = data["frame"]
    fps = data["fps"]

    if frame is None:
        break

    timestamp_ms = int(
        time.time() * 1000
    )

    processed_frame = preprocessor.pre_process(
        frame
    )

    results = humanDetector.detect_human(processed_frame, timestamp_ms)

    people_pose_data = humanDetector.extract_landmarks(results,processed_frame.shape)

    if len(people_pose_data) == 0:
        cv2.imshow(
            "Motion Intelligence Engine",
            processed_frame
        )

        if cv2.waitKey(1) == ord('q'):
            break

        continue

    pose_data = people_pose_data[0]

    smoothed_pose = tracker.smoothing(pose_data)

    tracked_people = identity_tracker.update(
        [smoothed_pose]
    )

    segmentation_map = segmentor.segment(
        processed_frame
    )

    person_mask = segmentor.create_person_mask(
        segmentation_map
    )


    smooth_mask = segmentor.addGaussianBlur(
        person_mask
    )

    isolated_human = segmentor.extract_human(
        processed_frame,
        smooth_mask
    )

    output = processed_frame.copy()

    output = humanDetector.draw_connections(
        output,
        smoothed_pose
    )

    output = humanDetector.draw_trails(
        output,
        tracker.history
    )

    output = identity_tracker.draw_ids(output, tracked_people
    )

    output = cv2.addWeighted(
        output,
        0.7,
        isolated_human,
        0.3,
        0
    )

    cv2.imshow(
        "Motion Intelligence Engine",
        output
    )

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()