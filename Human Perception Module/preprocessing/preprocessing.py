import cv2
import numpy as np

class preprocessor:
    def __init__(self):
        self.target_width= 620
        self.target_height= 480

    def resize_frame(self, frame):
        resized = cv2.resize(
            frame,
            (self.target_width, self.target_height)
        )

        return resized
    
    def bgr_to_rgb(self, frame):

        rgb_cvt = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        return rgb_cvt
    
    def to_grayscale(self, frame):

        grayscaled = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        return grayscaled

    def normalize(self, frame):
        normalized = frame / 255.0

        return normalized

    def gaussian_blur(self, frame):
        blurred = cv2.GaussianBlur(
            frame,
            (5, 5),
            0
        )

        return blurred

    def equalize(self, gray):

        equalized = cv2.equalizeHist(gray)

        return equalized

    def pre_process(self, frame):

        resized_frame = self.resize_frame(frame)

        rgb_frame = self.bgr_to_rgb(resized_frame)

        blurred_frame = self.gaussian_blur(rgb_frame)

        normalized_frame = self.normalize(blurred_frame)

        return normalized_frame