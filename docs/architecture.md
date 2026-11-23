
# HandTrack — Software Architecture

## Overview

HandTrack uses OpenCV and MediaPipe to detect hand
landmarks in a live webcam stream.

## Components

### main.py
- Initializes the webcam.
- Captures video frames.
- Displays the processed video.
- Manages application shutdown.

### hand_tracker.py
- Loads the MediaPipe Hand Landmarker model.
- Converts frames to RGB.
- Detects hand landmarks.
- Draws the 21 landmarks and their connections.

## Processing Pipeline

1. Capture a video frame with OpenCV.
2. Mirror the frame.
3. Convert the frame from BGR to RGB.
4. Run MediaPipe hand landmark detection.
5. Convert normalized landmarks into pixel coordinates.
6. Draw landmarks and connections.
7. Display the annotated frame.

## Design Decisions

- Use the MediaPipe Tasks API.
- Use VIDEO mode for synchronous frame processing.
- Limit detection to one hand in version 1.0.
- Separate webcam management from hand detection.
- Keep the pretrained model outside version control.


## Finger Counting

The `finger_counter.py` module analyzes the geometry
of the 21 detected hand landmarks.

It determines the state of each finger using:
- Joint angles
- Distances relative to the wrist or palm
- Geometric thresholds

The module provides two functions:

- `get_finger_states()`: returns the state of each finger.
- `count_fingers()`: returns the number of raised fingers.

This logic is independent of MediaPipe and OpenCV,
allowing automated unit testing.


## Gesture Recognition

The `gesture_detector.py` module classifies hand
gestures using individual finger states.

### Supported Gestures

- Fist: all five fingers are folded.
- Open Palm: all five fingers are raised.
- Victory: index and middle fingers are raised,
  while the remaining fingers are folded.
- Unknown: any other finger configuration.

### Temporal Stabilization

The GestureStabilizer class confirms a gesture
after four consecutive matching predictions.

This reduces short-term classification flickering.

The stabilizer is reset whenever no hand is detected.

### Limitations

Gesture classification depends on finger-counting
accuracy and the quality of hand landmark detection.


## Gesture-Based Visual Actions

The `gesture_actions.py` module manages visual
responses associated with recognized hand gestures.

### Supported Actions

| Gesture | Visual Action |
|---|---|
| Fist | Red border and ALERT state |
| Open Palm | Green border and READY state |
| Victory | Blue border and SUCCESS state |
| Unknown | Neutral WAITING state |
| No Hand | Neutral NO HAND state |

### Event Management

The GestureActionController monitors transitions
between stable hand gestures.

A new action is triggered only when the confirmed
gesture changes to a recognized gesture.

Holding the same gesture does not repeatedly
trigger the action.

The controller maintains an action counter during
the application session.

### Visual Feedback

The interface displays:

- A colored border representing the active state.
- A status message identifying the action.
- A counter of triggered actions.
- A brief notification when an action is triggered.

### Architecture Decision

Gesture classification and visual action management
are implemented in separate modules.

This separation improves maintainability and
allows independent automated testing.


## Final Architecture — Version 1.0

HandTrack follows a modular processing pipeline:

1. OpenCV captures webcam frames.
2. MediaPipe detects the 21 hand landmarks.
3. The finger counter determines individual finger states.
4. The gesture detector classifies predefined gestures.
5. A temporal stabilizer confirms consistent predictions.
6. The action controller generates interactive visual feedback.
7. OpenCV renders the annotated video.

## Separation of Responsibilities

- main.py: application orchestration and webcam lifecycle
- hand_tracker.py: landmark detection and visualization
- finger_counter.py: geometric finger analysis
- gesture_detector.py: classification and stabilization
- gesture_actions.py: interactive feedback and event counting

## Technical Limitations

- Only one hand is analyzed at a time.
- Finger counting uses 2D geometric heuristics.
- Strong hand rotation and occlusion can affect accuracy.
- Visual feedback depends on the reliability of gesture recognition.
- The action counter exists only during the current session.

## Privacy

HandTrack processes webcam frames locally.
The application does not automatically upload
or store captured video.

