import mediapipe as mp
import cv2

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HumanDetector:

    def __init__(self):

        # Model Configuration
        base_options = python.BaseOptions(
            model_asset_path='Human Perception Module\models\pose_landmarker_full.task'
        )

        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.VIDEO,
            num_poses=1,
            min_pose_detection_confidence=0.5,
            min_pose_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # Detector Initialization
        self.detector = vision.PoseLandmarker.create_from_options(
            options
        )

    def detect_human(self, frame, timestamp_ms):

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

    def extract_landmarks(self, results):

        landmark_data = []

        if results.pose_landmarks:

            for pose_landmarks in results.pose_landmarks:

                current_pose = []

                for id, landmark in enumerate(pose_landmarks):

                    current_pose.append({

                        "id": id,

                        "x": landmark.x,
                        "y": landmark.y,
                        "z": landmark.z,

                        "visibility": landmark.visibility

                    })

                landmark_data.append(current_pose)

        return landmark_data