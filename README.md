# Webcam Streaming Service

This project is a simple web application that captures images from the server's webcam and streams them to a web page in real-time. It utilizes Flask for the web framework and OpenCV for handling webcam interactions.

## Project Structure

```
webcam-streaming-service
├── src
│   ├── app.py                # Entry point of the application
│   ├── camera
│   │   └── webcam.py         # Webcam interaction logic
│   ├── streaming
│   │   └── stream_handler.py  # Video streaming functionality
│   └── static
│       ├── css
│       │   └── style.css     # CSS styles for the web page
│       └── js
│           └── app.js        # Client-side JavaScript logic
├── templates
│   └── index.html            # Main HTML template
├── requirements.txt          # Project dependencies
├── config.py                 # Configuration settings
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd webcam-streaming-service
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Flask application by running:
   ```
   python src/app.py
   ```

4. **Access the stream**:
   Open your web browser and navigate to `http://localhost:5000` to view the webcam stream.

## Usage Guidelines

- Ensure that your server has a webcam connected and accessible.
- Adjust the settings in `config.py` if necessary to match your webcam configuration.
- The application streams video in real-time, so ensure your network can handle the data transmission.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.