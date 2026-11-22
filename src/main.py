
from pathlib import Path

import cv2

from src.hand_tracker import HandTracker
from src.finger_counter import get_finger_states
from src.gesture_detector import (
    classify_gesture,
    GestureStabilizer
)


WINDOW_NAME = "HandTrack - Hand Detection"

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "hand_landmarker.task"
)


def main():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        camera.release()
        raise RuntimeError("Unable to open the webcam.")

    tracker = None
    gesture_stabilizer = GestureStabilizer(required_frames=4)

    print("HandTrack started.")
    print("Press Q to quit.")

    try:
        tracker = HandTracker(MODEL_PATH)

        while True:
            success, frame = camera.read()

            if not success or frame is None:
                print("Error: unable to read webcam frame.")
                break

            # Mirror the webcam image
            frame = cv2.flip(frame, 1)

            # Detect hand landmarks
            result = tracker.detect(frame)

            # Draw hand skeleton
            tracker.draw_landmarks(frame, result)

            # Analyze finger states and recognize gestures
            if result.hand_landmarks:
                landmarks = result.hand_landmarks[0]

                height, width = frame.shape[:2]

                # Get individual finger states
                finger_states = get_finger_states(
                    landmarks, width, height
                )

                # Count raised fingers
                finger_count = sum(finger_states.values())
                finger_text = f"Fingers: {finger_count}"

                # Classify the current gesture
                raw_gesture = classify_gesture(finger_states)

                # Stabilize gesture recognition
                gesture = gesture_stabilizer.update(raw_gesture)
                gesture_text = f"Gesture: {gesture}"

            else:
                finger_text = "Fingers: -"
                gesture_stabilizer.reset()
                gesture_text = "Gesture: No Hand"

            # Display detection status
            if result.hand_landmarks:
                status = "Hand detected"
                color = (0, 255, 0)
            else:
                status = "No hand detected"
                color = (0, 0, 255)

            cv2.putText(
                frame,
                status,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            cv2.putText(
                frame,
                "Press Q to quit",
                (20, 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                finger_text,
                (20, 115),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 255, 0),
                2
            )

            # Display recognized gesture
            cv2.putText(
                frame,
                gesture_text,
                (20, 155),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

            cv2.imshow(WINDOW_NAME, frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()

        if tracker is not None:
            tracker.close()

        print("HandTrack stopped.")


if __name__ == "__main__":
    main()
