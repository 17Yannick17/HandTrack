
from types import SimpleNamespace

import pytest

from src.finger_counter import (
    count_fingers,
    get_finger_states,
)


FINGERS = {"thumb", "index", "middle", "ring", "pinky"}


def make_landmarks(raised):
    """Create synthetic hand landmark coordinates."""
    def point(x, y):
        return SimpleNamespace(x=x, y=y)

    landmarks = [point(0.5, 0.92) for _ in range(21)]

    # Thumb
    landmarks[1] = point(0.35, 0.80)
    landmarks[2] = point(0.27, 0.71)

    if "thumb" in raised:
        landmarks[3] = point(0.19, 0.63)
        landmarks[4] = point(0.11, 0.55)
    else:
        landmarks[3] = point(0.34, 0.65)
        landmarks[4] = point(0.48, 0.66)

    # Other four fingers
    fingers = [
        ("index", 5, 0.41),
        ("middle", 9, 0.49),
        ("ring", 13, 0.57),
        ("pinky", 17, 0.65),
    ]

    for name, base, x in fingers:
        landmarks[base] = point(x, 0.63)

        if name in raised:
            ys = (0.48, 0.36, 0.25)
        else:
            ys = (0.51, 0.57, 0.64)

        for offset, y in enumerate(ys, start=1):
            landmarks[base + offset] = point(x, y)

    return landmarks


@pytest.mark.parametrize(
    "raised, expected",
    [
        (set(), 0),
        ({"index"}, 1),
        ({"thumb"}, 1),
        ({"index", "middle"}, 2),
        ({"index", "middle", "ring"}, 3),
        (FINGERS - {"thumb"}, 4),
        (FINGERS, 5),
    ],
)
def test_finger_count(raised, expected):
    landmarks = make_landmarks(raised)

    assert count_fingers(
        landmarks, 640, 480
    ) == expected


def test_finger_states():
    landmarks = make_landmarks({"index", "middle"})

    states = get_finger_states(landmarks, 640, 480)

    assert states["index"] is True
    assert states["middle"] is True
    assert states["thumb"] is False
    assert states["ring"] is False
    assert states["pinky"] is False


def test_mirrored_hand():
    landmarks = make_landmarks({"thumb", "index"})

    mirrored = [
        SimpleNamespace(x=1 - p.x, y=p.y)
        for p in landmarks
    ]

    assert count_fingers(mirrored, 640, 480) == 2


def test_invalid_landmarks():
    with pytest.raises(ValueError):
        count_fingers([], 640, 480)


def test_invalid_dimensions():
    landmarks = make_landmarks({"index"})

    with pytest.raises(ValueError):
        count_fingers(landmarks, 0, 480)
