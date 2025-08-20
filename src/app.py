
import os
from flask import Flask, render_template, Response
from camera.webcam import Webcam
from streaming.stream_handler import stream_video
from config import Config

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
app.config.from_object(Config)
webcam = Webcam(
    camera_index=app.config['WEBCAM_INDEX'],
    width=app.config['FRAME_WIDTH'],
    height=app.config['FRAME_HEIGHT'],
    fps=app.config['FRAME_RATE'],
    rotation=app.config['ROTATION_ANGLE']
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(stream_video(webcam), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(
        host=app.config['SERVER_HOST'],
        port=app.config['SERVER_PORT'],
        debug=app.config['DEBUG']
    )