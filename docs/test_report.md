
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



