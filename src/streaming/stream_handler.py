from flask import Response
from camera.webcam import Webcam

import time
from config import Config

def stream_video(webcam):
    def generate_frames():
        delay = 1.0 / Config.FRAME_RATE
        while True:
            start = time.time()
            frame = webcam.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            elapsed = time.time() - start
            if elapsed < delay:
                time.sleep(delay - elapsed)
    return generate_frames()