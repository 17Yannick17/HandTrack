
# HandTrack

**Real-Time Hand Tracking and Gesture Recognition Using Python**

HandTrack is a computer vision application that uses a webcam to detect and track hands, count raised fingers, and recognize predefined hand gestures in real time.

The project demonstrates computer vision, geometric analysis, real-time video processing, software testing, and structured software development practices.

## Features

### Completed

- Real-time webcam capture using OpenCV.
- Hand detection using MediaPipe Hand Landmarker.
- Visualization of 21 hand landmarks and their connections.
- Real-time hand movement tracking.
- Finger counting from 0 to 5.
- Individual finger state detection.
- Automated unit tests for finger counting.
- Webcam error handling and resource cleanup.

### In Development

- Recognition of three predefined gestures:
  - **Fist** — All fingers folded.
  - **Open Palm** — All fingers raised.
  - **Victory** — Index and middle fingers raised.
- Unknown gesture classification.
- Temporal gesture stabilization.
- Automated gesture recognition tests.

### Planned

- Gesture-based visual feedback and actions.
- Final integration testing.
- Application demonstration.
- Version 1.0 release.

## Technologies

| Technology | Purpose |
|---|---|
| Python 3.14 | Programming language |
| OpenCV | Webcam capture and image processing |
| MediaPipe | Hand landmark detection and tracking |
| NumPy | Numerical operations |
| pytest | Automated unit testing |
| Git | Version control |
| GitHub | Project management and collaboration |
| PyCharm | Development environment |

HandTrack uses a pretrained MediaPipe Hand Landmarker model. No custom model training is required.

## Project Structure

```text
HandTrack/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── hand_tracker.py
│   ├── finger_counter.py
│   └── gesture_detector.py
│
├── tests/
│   ├── test_finger_counter.py
│   └── test_gesture_detector.py
│
├── models/
│   ├── README.md
│   └── hand_landmarker.task
│
├── docs/
│   ├── requirements.md
│   ├── architecture.md
│   └── test_report.md
│
├── .gitignore
├── requirements.txt
└── README.md
```

The gesture recognition files are being added during Issue #4.

The virtual environment (`.venv`) and downloaded model file (`hand_landmarker.task`) are excluded from version control.

## Installation

### Prerequisites

- Python 3.14 or another version compatible with the dependencies.
- Git.
- A working webcam.
- A compatible operating system.

The project is developed and tested locally using PyCharm on Windows.

### Step 1 — Clone the Repository

```cmd
git clone https://github.com/17Yannick17/HandTrack.git
cd HandTrack
```

### Step 2 — Create a Virtual Environment

```cmd
python -m venv .venv
```

Activate the environment using Windows CMD:

```cmd
.venv\Scripts\activate
```

### Step 3 — Install Dependencies

```cmd
python -m pip install -r requirements.txt
```

### Step 4 — Download the MediaPipe Model

Create the model directory if necessary:

```cmd
mkdir models
```

Download the pretrained model:

```cmd
curl.exe -L --fail "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task" -o "models\hand_landmarker.task"
```

The model must be located at:

`models/hand_landmarker.task`

See [Model Documentation](models/README.md) for additional details.

## Usage

Run the application from the project root:

```cmd
python -m src.main
```

The application opens a window displaying the webcam stream.

### Instructions

1. Position your hand in front of the webcam.
2. Wait for the hand landmarks to appear.
3. Move your hand and observe the tracking.
4. Raise different fingers to test finger counting.
5. During Issue #4, test Fist, Open Palm, and Victory gestures.
6. Press **Q** to close the application.

## How It Works

HandTrack uses the following computer vision pipeline:

```text
Webcam
   |
   v
Video Capture (OpenCV)
   |
   v
Image Conversion (BGR to RGB)
   |
   v
Hand Landmark Detection (MediaPipe)
   |
   v
21 Hand Landmarks
   |
   v
Geometric Analysis
   |
   v
Individual Finger States
   |
   +----> Finger Counting (0-5)
   |
   v
Gesture Classification
   |
   v
Temporal Stabilization
   |
   v
Real-Time Visualization
```

### Hand Landmark Detection

MediaPipe identifies 21 landmarks corresponding to the wrist and finger joints.

These landmarks provide normalized spatial coordinates used for further analysis.

### Finger Counting

The finger-counting algorithm analyzes the geometry of the detected landmarks.

It uses:

- Joint angles.
- Distances between landmarks.
- Finger extension conditions.
- Palm-relative geometric measurements.

Each finger is classified as raised or folded.

The total number of raised fingers is then calculated.

### Gesture Recognition

The gesture recognition module uses individual finger states to classify predefined gestures.

| Gesture | Recognition Rule |
|---|---|
| Fist | All fingers folded |
| Open Palm | All fingers raised |
| Victory | Index and middle raised, others folded |
| Unknown | Any other configuration |

### Temporal Stabilization

A gesture must be detected in four consecutive frames before being confirmed.

This mechanism reduces short-term classification flickering.

When no hand is detected, the gesture state is reset.

## Testing

HandTrack includes automated unit tests and manual webcam validation.

### Automated Tests

Run the complete test suite:

```cmd
python -m pytest tests/ -v
```

The tests cover:

- Finger counting from 0 to 5.
- Individual finger states.
- Mirrored hand configurations.
- Invalid landmark data.
- Gesture classification.
- Temporal gesture stabilization.
- Gesture transitions and reset behavior.

### Manual Tests

Manual testing covers:

- Webcam initialization and shutdown.
- Detection of the 21 hand landmarks.
- Hand tracking during movement.
- Finger counting.
- Recognition of predefined gestures.
- Recognition stability.
- Behavior when no hand is detected.

Actual test results are documented in [Test Report](docs/test_report.md).

## Project Management

HandTrack follows a lightweight software development lifecycle.

Development activities are organized using:

- GitHub Issues for task tracking.
- GitHub Projects for Kanban management.
- Feature branches for development.
- Pull Requests for code integration.
- Descriptive Git commits.
- Automated and manual testing.
- Technical documentation.

### Development Roadmap

| Issue | Feature | Status |
|---|---|---|
| #1 | Webcam Capture | Completed |
| #2 | Hand Landmark Detection | Completed |
| #3 | Finger Counting | Completed |
| #4 | Gesture Recognition | In Progress |
| #5 | Visual Feedback and Actions | Planned |
| #6 | Final Testing and Documentation | Planned |

Each feature is tested and documented before being merged into the main branch.

## Documentation

Additional documentation:

- [Project Requirements](docs/requirements.md)
- [Software Architecture](docs/architecture.md)
- [Test Report](docs/test_report.md)
- [Model Documentation](models/README.md)

## Known Limitations

- Only one hand is processed at a time.
- Recognition accuracy depends on lighting conditions.
- Occluded fingers may be classified incorrectly.
- Strong hand rotations may affect geometric calculations.
- Gesture classification depends on finger-state accuracy.
- Temporal stabilization introduces a small recognition delay.

## Future Improvements

Potential extensions include:

- Multi-hand recognition.
- Additional hand gestures.
- Gesture-controlled presentation slides.
- Gesture-based system volume control.
- More robust recognition using 3D landmarks.
- Performance monitoring and FPS display.

## References

- [MediaPipe Hand Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Python Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/)

---

**HandTrack — A Computer Vision Project Built with Python.**
