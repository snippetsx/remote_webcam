import cv2
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from config import Config

class Webcam:
    def __init__(self, camera_index=0, width=None, height=None, fps=None):
        self.camera_index = camera_index
        self.capture = cv2.VideoCapture(self.camera_index)
        # Set width, height, and fps from config or arguments
        width = width if width is not None else Config.FRAME_WIDTH
        height = height if height is not None else Config.FRAME_HEIGHT
        fps = fps if fps is not None else Config.FRAME_RATE
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.capture.set(cv2.CAP_PROP_FPS, fps)

    def __del__(self):
        if self.capture.isOpened():
            self.capture.release()

    def get_frame(self):
        ret, frame = self.capture.read()
        if not ret:
            return None
        _, buffer = cv2.imencode('.jpg', frame)
        return buffer.tobytes()