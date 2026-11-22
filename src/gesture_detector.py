
FINGER_NAMES = (
    "thumb",
    "index",
    "middle",
    "ring",
    "pinky"
)

FIST = "Fist"
OPEN_PALM = "Open Palm"
VICTORY = "Victory"
UNKNOWN = "Unknown"


def classify_gesture(finger_states):
    """Classify a gesture from individual finger states."""

    if not all(
        finger in finger_states for finger in FINGER_NAMES
    ):
        raise ValueError("Missing finger states.")

    # All fingers folded
    if all(
        not finger_states[finger]
        for finger in FINGER_NAMES
    ):
        return FIST

    # All fingers raised
    if all(
        finger_states[finger]
        for finger in FINGER_NAMES
    ):
        return OPEN_PALM

    # Index and middle raised, other fingers folded
    if (
        finger_states["index"]
        and finger_states["middle"]
        and not finger_states["thumb"]
        and not finger_states["ring"]
        and not finger_states["pinky"]
    ):
        return VICTORY

    return UNKNOWN


class GestureStabilizer:
    """Confirm gestures detected across consecutive frames."""

    def __init__(self, required_frames=4):
        if required_frames < 1:
            raise ValueError(
                "required_frames must be at least 1."
            )

        self.required_frames = required_frames
        self.reset()

    def reset(self):
        self.candidate = None
        self.consecutive_frames = 0
        self.stable_gesture = UNKNOWN

    def update(self, gesture):
        if gesture == self.candidate:
            self.consecutive_frames += 1
        else:
            self.candidate = gesture
            self.consecutive_frames = 1

        if self.consecutive_frames >= self.required_frames:
            self.stable_gesture = gesture

        return self.stable_gesture
