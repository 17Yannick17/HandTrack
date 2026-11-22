
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
