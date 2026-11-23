
import cv2

from src.gesture_detector import (
    FIST,
    OPEN_PALM,
    VICTORY,
    UNKNOWN,
)


class GestureActionController:
    """Manage visual actions triggered by recognized gestures."""

    # OpenCV uses BGR colors
    ACTIONS = {
        FIST: ("ALERT", (0, 0, 255)),
        OPEN_PALM: ("READY", (0, 180, 0)),
        VICTORY: ("SUCCESS", (255, 120, 0)),
    }

    NEUTRAL_COLOR = (110, 110, 110)

    def __init__(self):
        self.current_gesture = UNKNOWN
        self.event_count = 0
        self.flash_frames = 0

    def update(self, gesture):
        """Trigger an action when a confirmed gesture changes."""

        if gesture not in self.ACTIONS and gesture != UNKNOWN:
            raise ValueError(f"Unsupported gesture: {gesture}")

        if gesture == self.current_gesture:
            return False

        self.current_gesture = gesture
        self.flash_frames = 0

        if gesture in self.ACTIONS:
            self.event_count += 1
            self.flash_frames = 12
            return True

        return False

    def reset(self):
        """Clear the active action without resetting event history."""
        self.current_gesture = UNKNOWN
        self.flash_frames = 0

    def draw(self, frame, hand_detected=True):
        """Draw visual feedback directly on the video frame."""

        height, width = frame.shape[:2]

        if not hand_detected:
            label = "NO HAND"
            color = self.NEUTRAL_COLOR

        else:
            label, color = self.ACTIONS.get(
                self.current_gesture,
                ("WAITING", self.NEUTRAL_COLOR)
            )

        # Draw a colored frame border
        border_thickness = (
            8 if self.flash_frames > 0 else 4
        )

        cv2.rectangle(
            frame,
            (3, 3),
            (width - 4, height - 4),
            color,
            border_thickness
        )

        # Draw bottom action panel
        cv2.rectangle(
            frame,
            (0, height - 80),
            (width - 1, height - 1),
            color,
            -1
        )

        cv2.putText(
            frame,
            f"ACTION: {label}",
            (20, height - 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Actions triggered: {self.event_count}",
            (20, height - 17),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )

        # Brief notification for new actions
        if self.flash_frames > 0:
            cv2.putText(
                frame,
                "NEW ACTION",
                (max(20, width - 200), 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.65,
                (255, 255, 255),
                2
            )

            self.flash_frames -= 1
