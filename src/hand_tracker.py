
import time
from pathlib import Path

import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self, model_path: Path):
        if not model_path.is_file():
            raise FileNotFoundError(
                f"Hand Landmarker model not found: {model_path}"
            )

        # Configure MediaPipe
        options = mp.tasks.vision.HandLandmarkerOptions(
            base_options=mp.tasks.BaseOptions(
                model_asset_path=str(model_path)
            ),
            running_mode=mp.tasks.vision.RunningMode.VIDEO,
            num_hands=1,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5,
        )

        self.landmarker = (
            mp.tasks.vision.HandLandmarker.create_from_options(options)
        )

        self.last_timestamp_ms = -1

    def detect(self, frame):
        # Convert OpenCV BGR to MediaPipe RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        # MediaPipe VIDEO mode requires increasing timestamps
        timestamp_ms = max(
            time.monotonic_ns() // 1_000_000,
            self.last_timestamp_ms + 1
        )
        self.last_timestamp_ms = timestamp_ms

        return self.landmarker.detect_for_video(
            mp_image, timestamp_ms
        )

    @staticmethod
    def draw_landmarks(frame, result):
        height, width = frame.shape[:2]

        connections = (
            mp.tasks.vision.HandLandmarksConnections.HAND_CONNECTIONS
        )

        for hand_landmarks in result.hand_landmarks:
            points = [
                (
                    int(landmark.x * width),
                    int(landmark.y * height)
                )
                for landmark in hand_landmarks
            ]

            # Draw connections between landmarks
            for connection in connections:
                cv2.line(
                    frame,
                    points[connection.start],
                    points[connection.end],
                    (0, 255, 0),
                    2
                )

            # Draw the 21 landmarks
            for point in points:
                cv2.circle(
                    frame,
                    point,
                    4,
                    (0, 0, 255),
                    -1
                )

    def close(self):
        self.landmarker.close()
