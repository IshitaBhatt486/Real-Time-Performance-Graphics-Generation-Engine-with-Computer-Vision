import cv2
import time

from config.settings import *

class Camera:

    def __init__(self):

        self.cap=cv2.VideoCapture(CAMERA_ID)

        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            FRAME_WIDTH
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            FRAME_HEIGHT
        )

        self.cap.set(
            cv2.CAP_PROP_FPS,
            FPS
        )

        self.previous_time=0
        self.frame_count=0


    def get_frame(self):

        ret,frame=self.cap.read()

        if not ret:
            return None

        self.frame_count+=1

        current=time.time()

        fps=1/(current-self.previous_time) if self.previous_time!=0 else 0

        self.previous_time=current

        return {

            "frame":frame,
            "fps":fps,
            "timestamp":current,
            "frame_number":self.frame_count

        }


    def release(self):

        self.cap.release()