
import pytest

from src.gesture_detector import (
    FINGER_NAMES,
    FIST,
    OPEN_PALM,
    VICTORY,
    UNKNOWN,
    GestureStabilizer,
    classify_gesture,
)


def make_states(raised):
    return {
        name: name in raised
        for name in FINGER_NAMES
    }


@pytest.mark.parametrize(
    "raised, expected",
    [
        (set(), FIST),
        (set(FINGER_NAMES), OPEN_PALM),
        ({"index", "middle"}, VICTORY),
        ({"index"}, UNKNOWN),
        ({"thumb", "index", "middle"}, UNKNOWN),
        ({"thumb", "index", "middle", "ring"}, UNKNOWN),
        ({"index", "middle", "pinky"}, UNKNOWN),
    ]
)
def test_gesture_classification(raised, expected):
    states = make_states(raised)
    assert classify_gesture(states) == expected


def test_missing_finger_states():
    with pytest.raises(ValueError):
        classify_gesture({"index": True})


def test_gesture_stabilization():
    stabilizer = GestureStabilizer(required_frames=4)

    for _ in range(3):
        assert stabilizer.update(VICTORY) == UNKNOWN

    assert stabilizer.update(VICTORY) == VICTORY


def test_single_frame_noise():
    stabilizer = GestureStabilizer(required_frames=4)

    for _ in range(4):
        stabilizer.update(OPEN_PALM)

    assert stabilizer.update(FIST) == OPEN_PALM


def test_gesture_transition():
    stabilizer = GestureStabilizer(required_frames=4)

    for _ in range(4):
        stabilizer.update(FIST)

    for _ in range(3):
        assert stabilizer.update(VICTORY) == FIST

    assert stabilizer.update(VICTORY) == VICTORY


def test_stabilizer_reset():
    stabilizer = GestureStabilizer(required_frames=4)

    for _ in range(4):
        stabilizer.update(FIST)

    stabilizer.reset()

    assert stabilizer.stable_gesture == UNKNOWN
    assert stabilizer.update(FIST) == UNKNOWN


def test_invalid_stabilizer_configuration():
    with pytest.raises(ValueError):
        GestureStabilizer(required_frames=0)
