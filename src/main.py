
from pathlib import Path

import cv2

from src.hand_tracker import HandTracker
from src.finger_counter import get_finger_states
from src.gesture_detector import (
    classify_gesture,
    GestureStabilizer,
)
from src.gesture_actions import GestureActionController


WINDOW_NAME = "HandTrack - Gesture Recognition"

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

    gesture_stabilizer = GestureStabilizer(
        required_frames=4
    )

    action_controller = GestureActionController()

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

            # Detect and draw hand landmarks
            result = tracker.detect(frame)
            tracker.draw_landmarks(frame, result)

            if result.hand_landmarks:
                landmarks = result.hand_landmarks[0]

                height, width = frame.shape[:2]

                # Analyze individual finger states
                finger_states = get_finger_states(
                    landmarks, width, height
                )

                finger_count = sum(
                    finger_states.values()
                )

                finger_text = (
                    f"Fingers: {finger_count}"
                )

                # Classify and stabilize the gesture
                raw_gesture = classify_gesture(
                    finger_states
                )

                gesture = gesture_stabilizer.update(
                    raw_gesture
                )

                gesture_text = (
                    f"Gesture: {gesture}"
                )

                status = "Hand detected"
                status_color = (0, 255, 0)

                # Trigger visual action
                action_controller.update(gesture)

                hand_detected = True

            else:
                finger_text = "Fingers: -"
                gesture_text = "Gesture: No Hand"

                status = "No hand detected"
                status_color = (0, 0, 255)

                gesture_stabilizer.reset()
                action_controller.reset()

                hand_detected = False

            # Display hand detection status
            cv2.putText(
                frame,
                status,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                status_color,
                2
            )

            # Display instructions
            cv2.putText(
                frame,
                "Press Q to quit",
                (20, 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

            # Display finger count
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

            # Draw interactive visual feedback
            action_controller.draw(
                frame,
                hand_detected=hand_detected
            )

            # Show the processed video
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
