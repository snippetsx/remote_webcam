const videoElement = document.getElementById('videoStream');

function startStream() {
    const source = new EventSource('/stream');
    source.onmessage = function(event) {
        videoElement.src = 'data:image/jpeg;base64,' + event.data;
    };
}

window.onload = startStream;