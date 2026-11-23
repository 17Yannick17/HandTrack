
import numpy as np
import pytest

from src.gesture_detector import (
    FIST,
    OPEN_PALM,
    VICTORY,
    UNKNOWN,
)
from src.gesture_actions import GestureActionController


@pytest.mark.parametrize(
    "gesture",
    [FIST, OPEN_PALM, VICTORY]
)
def test_valid_gesture_triggers_action(gesture):
    controller = GestureActionController()

    triggered = controller.update(gesture)

    assert triggered is True
    assert controller.event_count == 1
    assert controller.current_gesture == gesture


def test_same_gesture_does_not_repeat_action():
    controller = GestureActionController()

    controller.update(FIST)
    triggered = controller.update(FIST)

    assert triggered is False
    assert controller.event_count == 1


def test_gesture_transition_triggers_new_action():
    controller = GestureActionController()

    controller.update(FIST)
    triggered = controller.update(VICTORY)

    assert triggered is True
    assert controller.event_count == 2


def test_unknown_gesture_does_not_trigger_action():
    controller = GestureActionController()

    triggered = controller.update(UNKNOWN)

    assert triggered is False
    assert controller.event_count == 0


def test_unknown_allows_future_retrigger():
    controller = GestureActionController()

    controller.update(FIST)
    controller.update(UNKNOWN)
    controller.update(FIST)

    assert controller.event_count == 2


def test_reset_clears_active_action():
    controller = GestureActionController()

    controller.update(OPEN_PALM)
    controller.reset()

    assert controller.current_gesture == UNKNOWN
    assert controller.event_count == 1
    assert controller.flash_frames == 0


def test_action_after_reset():
    controller = GestureActionController()

    controller.update(VICTORY)
    controller.reset()

    triggered = controller.update(VICTORY)

    assert triggered is True
    assert controller.event_count == 2


def test_invalid_gesture():
    controller = GestureActionController()

    with pytest.raises(ValueError):
        controller.update("Invalid Gesture")


def test_visual_feedback_draws_on_frame():
    controller = GestureActionController()
    controller.update(FIST)

    frame = np.zeros((480, 640, 3), dtype=np.uint8)

    controller.draw(frame)

    assert np.any(frame != 0)
    assert controller.flash_frames == 11


def test_visual_feedback_without_hand():
    controller = GestureActionController()

    frame = np.zeros((480, 640, 3), dtype=np.uint8)

    controller.draw(frame, hand_detected=False)

    assert np.any(frame != 0)
    assert controller.event_count == 0
