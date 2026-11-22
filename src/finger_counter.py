
from math import acos, degrees, hypot


FINGER_JOINTS = {
    "index": (5, 6, 8),
    "middle": (9, 10, 12),
    "ring": (13, 14, 16),
    "pinky": (17, 18, 20),
}


def distance(a, b, width, height):
    """Calculate the distance between two landmarks in pixels."""
    dx = (a.x - b.x) * width
    dy = (a.y - b.y) * height
    return hypot(dx, dy)


def joint_angle(a, b, c, width, height):
    """Calculate angle ABC in degrees."""
    ux = (a.x - b.x) * width
    uy = (a.y - b.y) * height

    vx = (c.x - b.x) * width
    vy = (c.y - b.y) * height

    magnitude = hypot(ux, uy) * hypot(vx, vy)

    if magnitude == 0:
        return 0.0

    cosine = (ux * vx + uy * vy) / magnitude
    cosine = max(-1.0, min(1.0, cosine))

    return degrees(acos(cosine))


def get_finger_states(landmarks, width, height):
    """Return True for each finger considered raised."""
    if len(landmarks) != 21:
        raise ValueError("Exactly 21 hand landmarks are required.")

    if width <= 0 or height <= 0:
        raise ValueError("Invalid frame dimensions.")

    states = {}

    # Thumb: use joint angles and palm-relative distance
    thumb_base_angle = joint_angle(
        landmarks[1], landmarks[2], landmarks[3],
        width, height
    )

    thumb_tip_angle = joint_angle(
        landmarks[2], landmarks[3], landmarks[4],
        width, height
    )

    palm_width = distance(
        landmarks[5], landmarks[17], width, height
    )

    thumb_distance = distance(
        landmarks[4], landmarks[17], width, height
    )

    states["thumb"] = (
        thumb_base_angle >= 145
        and thumb_tip_angle >= 150
        and thumb_distance > palm_width
    )

    # Index, middle, ring and pinky
    for name, (mcp, pip, tip) in FINGER_JOINTS.items():
        angle = joint_angle(
            landmarks[mcp],
            landmarks[pip],
            landmarks[tip],
            width,
            height
        )

        tip_distance = distance(
            landmarks[tip], landmarks[0],
            width, height
        )

        pip_distance = distance(
            landmarks[pip], landmarks[0],
            width, height
        )

        states[name] = (
            angle >= 155
            and tip_distance > pip_distance * 1.05
        )

    return states


def count_fingers(landmarks, width, height):
    """Count the number of raised fingers."""
    states = get_finger_states(landmarks, width, height)
    return sum(states.values())
