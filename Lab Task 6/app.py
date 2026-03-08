import cv2
import time
import mediapipe as mp
from flask import Flask, render_template, Response
from gesture_classifier import classify_gesture, count_fingers

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

app = Flask(__name__)

latest_result = None

def print_result(result, output_image, timestamp_ms):
    global latest_result
    latest_result = result

def initialize_hand_landmarker():
    model_path = 'hand_landmarker.task'  # Must be in the same folder
    base_options = python.BaseOptions(model_asset_path=model_path)
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.LIVE_STREAM,
        num_hands=1,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
        result_callback=print_result
    )
    return vision.HandLandmarker.create_from_options(options)

hand_landmarker = initialize_hand_landmarker()
camera = cv2.VideoCapture(0)

# Hand connections (same as MediaPipe standard)
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),       # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),       # Index
    (0, 9), (9, 10), (10, 11), (11, 12),  # Middle
    (0, 13), (13, 14), (14, 15), (15, 16),# Ring
    (0, 17), (17, 18), (18, 19), (19, 20),# Pinky
    (5, 9), (9, 13), (13, 17)              # Palm connections
]

def draw_landmarks(image, landmarks):
    """
    Draw hand landmarks and connections on the image using OpenCV.
    landmarks: list of 21 NormalizedLandmark objects (with x, y, z)
    """
    h, w, _ = image.shape
    # Draw connections (lines)
    for connection in HAND_CONNECTIONS:
        start_idx, end_idx = connection
        start = landmarks[start_idx]
        end = landmarks[end_idx]
        start_point = (int(start.x * w), int(start.y * h))
        end_point = (int(end.x * w), int(end.y * h))
        cv2.line(image, start_point, end_point, (0, 255, 0), 2)

    # Draw landmarks (circles)
    for lm in landmarks:
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(image, (cx, cy), 4, (0, 0, 255), -1)  # Red filled circles

def generate_frames():
    global latest_result
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Mirror effect
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        timestamp_ms = int(time.time() * 1000)
        hand_landmarker.detect_async(mp_image, timestamp_ms)

        result = latest_result

        gesture_name = "No Hand"
        finger_count = 0
        if result and result.hand_landmarks:
            hand_landmarks = result.hand_landmarks[0]
            gesture_name = classify_gesture(hand_landmarks)
            finger_count = count_fingers(hand_landmarks)
            draw_landmarks(frame, hand_landmarks)

        # Overlay text
        cv2.putText(frame, f"Gesture: {gesture_name}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"Fingers: {finger_count}", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)