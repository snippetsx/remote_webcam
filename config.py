import os

class Config:
    """Configuration settings for the webcam streaming service."""
    
    # Webcam settings
    WEBCAM_INDEX = 0  # Index of the webcam to use
    FRAME_WIDTH = 1280  # Width of the video frame
    FRAME_HEIGHT = 720  # Height of the video frame
    FRAME_RATE = 30  # Frame rate for the video stream
    # Server settings
    SERVER_HOST = '0.0.0.0'  # Host to run the server on
    SERVER_PORT = 5000  # Port to run the server on
    
    # Other settings
    DEBUG = True  # Enable debug mode for development
    SECRET_KEY = os.urandom(24)  # Secret key for session management