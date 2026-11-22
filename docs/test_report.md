
# HandTrack — Test Report

## Issue #1: Webcam Capture

### Objective

Validate real-time video acquisition using OpenCV.

### Test Cases

| ID | Test | Expected Result | Status |
|---|---|---|---|
| T01 | Start with an available webcam | Video is displayed | Passed |
| T02 | Press Q | Application closes normally | Passed |
| T03 | Use an invalid camera index | Clear error message | Passed |
| T04 | Restart the application | Webcam opens again | Passed |


## Issue #2 — Hand Landmark Detection

### Objective

Validate real-time hand landmark detection using MediaPipe.

### Test Cases

| ID | Test | Expected Result | Status |
|---|---|---|---|
| T05 | Present one open hand | 21 landmarks displayed | Passed |
| T06 | Move the hand | Landmarks follow the movement | Passed |
| T07 | Remove the hand | No hand detected | Passed |
| T08 | Present two hands | At most one hand is tracked | Passed |
| T09 | Run without model file | Clear error message | Passed |
| T10 | Press Q | Application closes correctly | Passed |

### Known Limitations

- One hand is processed at a time.
- Detection can be affected by poor lighting and occlusion.
- Finger counting is not implemented yet.


## Issue #3 — Finger Counting

### Objective

Validate finger counting from 0 to 5 using hand landmarks.

### Automated Tests

Run:

`python -m pytest tests/ -v`

Result: To be completed after execution.

### Manual Tests

| ID | Scenario | Expected | Status |
|---|---|---|---|
| T11 | Closed fist | 0 fingers | Passed |
| T12 | Index raised | 1 finger | Passed |
| T13 | Victory gesture | 2 fingers | Passed |
| T14 | Three fingers raised | 3 fingers | Passed |
| T15 | Four fingers raised | 4 fingers | Passed |
| T16 | Open hand | 5 fingers | Passed |
| T17 | No hand visible | Display "-" | Passed |
| T18 | Left and right hands | Correct count | Passed |

### Known Limitations

- The algorithm uses 2D landmark geometry.
- Strong rotations and occlusions may reduce accuracy.
- Thresholds may require further calibration.



## Issue #4 — Gesture Recognition

### Objective

Validate predefined hand gesture recognition.

### Automated Tests

Command:

`python -m pytest tests/ -v`

Result: To be completed after execution.

### Manual Tests

| ID | Test | Expected Result | Status |
|---|---|---|---|
| T19 | Closed fist | Fist | Passed |
| T20 | Open hand | Open Palm | Passed |
| T21 | Victory sign | Victory | Passed |
| T22 | Index finger raised | Unknown | Passed |
| T23 | Remove hand | No Hand | Passed |
| T24 | Quickly change gestures | Stable recognition | Passed |
| T25 | Left and right hands | Correct recognition | Passed |

### Known Limitations

- Recognition depends on finger-counting accuracy.
- Strong rotations may affect finger-state detection.
- Gestures require four consecutive matching frames
  before confirmation.




