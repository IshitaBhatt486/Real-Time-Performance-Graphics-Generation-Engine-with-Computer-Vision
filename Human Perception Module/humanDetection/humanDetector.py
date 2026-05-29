import mediapipe as mp
import cv2

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from humanDetection.landmarks import LANDMARK_NAMES, POSE_CONNECTIONS

no_of_performers = 5

class HumanDetector:

    def __init__(self):

        # Model Configuration
        base_options = python.BaseOptions(
            model_asset_path='Human Perception Module\models\pose_landmarker_full.task'
        )

        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.VIDEO,
            num_poses=no_of_performers,
            min_pose_detection_confidence=0.5,
            min_pose_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # Detector Initialization
        self.detector = vision.PoseLandmarker.create_from_options(
            options
        )

    def detect_human(self, frame, timestamp_ms):

        frame = frame.astype("uint8")

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        results = self.detector.detect_for_video(
            mp_image,
            timestamp_ms
        )

        return results

    def draw_landmarks(self, frame, results):

        height, width, _ = frame.shape

        if results.pose_landmarks:

            for pose_landmarks in results.pose_landmarks:

                for landmark in pose_landmarks:

                    x = int(landmark.x * width)
                    y = int(landmark.y * height)

                    cv2.circle(
                        frame,
                        (x, y),
                        5,
                        (0, 255, 0),
                        -1
                    )

        return frame

    def extract_landmarks(
        self,
        results,
        frame_shape
    ):

        people_pose_data = []
        height,width,_ = frame_shape

        if results.pose_landmarks:

            for pose_landmarks in results.pose_landmarks:

                pose_data = {}

                for id, landmark in enumerate(
                    pose_landmarks
                ):

                    if id not in LANDMARK_NAMES:
                        continue

                    if landmark.visibility < 0.5:
                        continue

                    px = int(landmark.x * width)
                    py = int(landmark.y * height)

                    pose_data[
                        LANDMARK_NAMES[id]
                    ] = {

                        "x":px,
                        "y":py,
                        "z":landmark.z,

                        "visibility":
                        landmark.visibility

                    }

                people_pose_data.append(
                    pose_data
                )

        return people_pose_data
    
    def draw_connections(self, frame, pose_data):
        for p1,p2 in POSE_CONNECTIONS:

            if p1 in pose_data and p2 in pose_data:

                x1 = pose_data[p1]["x"]
                y1 = pose_data[p1]["y"]

                x2 = pose_data[p2]["x"]
                y2 = pose_data[p2]["y"]

                cv2.line(
                    frame,
                    (x1,y1),
                    (x2,y2),
                    (255,0,0),
                    2
                )

        return frame

    def draw_trails(
        self,
        frame,
        history
    ):
        for joint in history:

            points = history[joint]

            for point in points:

                cv2.circle(
                    frame,
                    point,
                    2,
                    (0,0,255),
                    -1
                )

        return frame