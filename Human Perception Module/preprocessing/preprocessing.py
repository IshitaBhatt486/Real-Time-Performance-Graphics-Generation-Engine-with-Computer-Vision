import cv2

class preprocessor:

    def __init__(self):
        self.target_width = 640
        self.target_height = 480

    def resize_frame(
        self,
        frame
    ):
        resized = cv2.resize(
            frame,
            (
                self.target_width,
                self.target_height
            )
        )
        return resized

    def gaussian_blur(
        self,
        frame
    ):
        blurred = cv2.GaussianBlur(
            frame,
            (5,5),
            0
        )
        return blurred

    def pre_process(
        self,
        frame
    ):

        resized_frame = self.resize_frame(
            frame
        )

        blurred_frame = self.gaussian_blur(
            resized_frame
        )

        return blurred_frame