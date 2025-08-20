import cv2
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from config import Config

class Webcam:
    def __init__(self, camera_index=0, width=None, height=None, fps=None, rotation=0):
        self.camera_index = camera_index
        self.rotation = rotation  # Rotation angle in degrees
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
        
        # Apply rotation if specified
        if self.rotation != 0:
            frame = self.rotate_frame(frame, self.rotation)
        
        _, buffer = cv2.imencode('.jpg', frame)
        return buffer.tobytes()
    
    def rotate_frame(self, frame, angle):
        """Rotate frame by the specified angle in degrees."""
        height, width = frame.shape[:2]
        center = (width // 2, height // 2)
        
        # Get rotation matrix
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        
        # Calculate new bounding dimensions
        cos_val = abs(rotation_matrix[0, 0])
        sin_val = abs(rotation_matrix[0, 1])
        new_width = int((height * sin_val) + (width * cos_val))
        new_height = int((height * cos_val) + (width * sin_val))
        
        # Adjust rotation matrix for new center
        rotation_matrix[0, 2] += (new_width / 2) - center[0]
        rotation_matrix[1, 2] += (new_height / 2) - center[1]
        
        # Perform rotation
        rotated_frame = cv2.warpAffine(frame, rotation_matrix, (new_width, new_height))
        return rotated_frame