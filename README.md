
# HandTrack

**Real-Time Hand Tracking and Gesture Recognition Using Python**

HandTrack is a computer vision application that uses a webcam to detect and track a human hand, count raised fingers, recognize predefined hand gestures, and trigger interactive visual responses in real time.

The project demonstrates practical applications of computer vision, geometric analysis, real-time image processing, software testing, and structured software development.

## 1. Features

### Completed

- Real-time webcam capture using OpenCV.
- Hand detection using MediaPipe Hand Landmarker.
- Visualization of 21 hand landmarks.
- Real-time hand movement tracking.
- Finger counting from 0 to 5.
- Individual finger state detection.
- Recognition of three predefined hand gestures:
  - **Fist** — All fingers folded.
  - **Open Palm** — All fingers raised.
  - **Victory** — Index and middle fingers raised.
- Unknown gesture classification.
- Temporal stabilization of gesture recognition.
- Automated unit tests for finger counting and gesture recognition.
- Webcam error handling and resource cleanup.

### In Development

- Gesture-based visual actions.
- Color-coded feedback for recognized gestures.
- Visual action event counting.
- Automated testing of visual actions.

### Planned

- Final integration testing.
- Complete technical documentation.
- Application demonstration.
- Version 1.0 release.

## 2. Technologies

| Technology | Purpose |
|---|---|
| Python 3.14 | Programming language |
| OpenCV | Webcam capture and image processing |
| MediaPipe | Hand landmark detection and tracking |
| NumPy | Numerical operations |
| pytest | Automated testing |
| Git | Version control |
| GitHub | Project and issue management |
| PyCharm | Development environment |

HandTrack uses a pretrained MediaPipe Hand Landmarker model.

No custom machine learning training is required.

## 3. Project Structure

```text
HandTrack/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── hand_tracker.py
│   ├── finger_counter.py
│   ├── gesture_detector.py
│   └── gesture_actions.py
│
├── tests/
│   ├── test_finger_counter.py
│   ├── test_gesture_detector.py
│   └── test_gesture_actions.py
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

The virtual environment and pretrained model file are excluded from Git version control.

The visual action modules and associated tests are being integrated during Issue #5.

## 4. Installation

### Prerequisites

- Python 3.14 or another version supported by the dependencies.
- Git.
- A working webcam.
- A compatible operating system.

The project is developed locally using PyCharm on Windows.

### Step 1 — Clone the Repository

```cmd
git clone https://github.com/17Yannick17/HandTrack.git
cd HandTrack
```

### Step 2 — Create a Virtual Environment

```cmd
python -m venv .venv
```

Activate the environment on Windows CMD:

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

The model must be stored at:

`models/hand_landmarker.task`

See [Model Documentation](models/README.md).

## 5. Usage

Launch the application from the project root:

```cmd
python -m src.main
```

A window opens and displays the live webcam stream.

### Instructions

1. Present one hand in front of the webcam.
2. Observe the detected hand landmarks.
3. Raise different fingers to test finger counting.
4. Perform one of the supported gestures.
5. Observe the recognized gesture on the screen.
6. During Issue #5, test the corresponding visual actions.
7. Press **Q** to close the application.

### Supported Gestures

| Gesture | Finger Configuration | Visual Action |
|---|---|---|
| Fist | All fingers folded | Red ALERT mode |
| Open Palm | All fingers raised | Green READY mode |
| Victory | Index and middle raised | Blue SUCCESS mode |
| Unknown | Other configurations | Neutral WAITING mode |

The visual actions are being implemented during Issue #5.

## 6. How It Works

HandTrack follows a modular computer vision pipeline:

```text
Webcam
   |
   v
Video Capture (OpenCV)
   |
   v
BGR to RGB Conversion
   |
   v
Hand Landmark Detection (MediaPipe)
   |
   v
21 Hand Landmarks
   |
   v
Geometric Finger Analysis
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
Gesture Action Controller
   |
   v
Interactive Visual Feedback
```

### Hand Landmark Detection

MediaPipe identifies 21 landmarks corresponding to the wrist and finger joints.

These landmarks provide normalized coordinates used for geometric analysis.

### Finger Counting

Finger counting is based on geometric calculations:

- Joint angles.
- Distances between landmarks.
- Finger extension conditions.
- Palm-relative measurements.

Each finger is classified as raised or folded.

### Gesture Recognition

The `gesture_detector.py` module uses finger states to recognize predefined gestures.

A gesture is classified as Fist, Open Palm, Victory, or Unknown.

### Temporal Stabilization

A gesture must be detected in four consecutive frames before being confirmed.

This reduces short-term classification flickering.

The gesture state is reset when no hand is detected.

### Interactive Visual Actions

The `gesture_actions.py` module manages visual responses associated with confirmed gestures.

The interface is designed to display:

- A colored border for the active gesture.
- A visual action status.
- A counter of triggered actions.
- A short notification when a new action occurs.

An action is triggered once per transition to a recognized gesture, not once per video frame.

This feature is being developed during Issue #5.

## 7. Testing

HandTrack includes automated unit tests and manual webcam validation.

### Automated Tests

Run all tests using:

```cmd
python -m pytest tests/ -v
```

The test suite covers:

- Finger counting from 0 to 5.
- Individual finger states.
- Mirrored landmark configurations.
- Invalid input handling.
- Gesture classification.
- Temporal gesture stabilization.
- Gesture transitions.
- Visual action event management.

### Manual Tests

Manual testing includes:

- Webcam initialization and shutdown.
- Hand landmark detection.
- Hand movement tracking.
- Finger counting.
- Gesture recognition.
- Recognition stability.
- Visual feedback.
- Action event counting.
- Resource cleanup.

Actual test results are documented in the [Test Report](docs/test_report.md).

## 8. Project Management

HandTrack follows a lightweight software development lifecycle.

Project management practices include:

- GitHub Issues for task tracking.
- GitHub Projects for Kanban management.
- Dedicated feature branches.
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
| #4 | Gesture Recognition | Completed |
| #5 | Visual Feedback and Actions | In Progress |
| #6 | Final Testing and Documentation | Planned |

Each feature is tested and documented before integration into the main branch.

## 9. Documentation

Additional project documentation:

- [Project Requirements](docs/requirements.md)
- [Software Architecture](docs/architecture.md)
- [Test Report](docs/test_report.md)
- [Model Documentation](models/README.md)

## 10. Known Limitations

- Only one hand is processed at a time.
- Recognition accuracy depends on lighting conditions.
- Finger occlusions may cause classification errors.
- Strong hand rotations can affect geometric calculations.
- Gesture recognition depends on finger-state accuracy.
- Temporal stabilization introduces a short delay.
- Visual actions do not control external applications.
- The action counter is not persistent between sessions.

## 11. Future Improvements

Potential extensions include:

- Multi-hand tracking.
- Additional predefined gestures.
- Gesture-based presentation controls.
- Gesture-controlled system volume.
- Improved recognition using 3D landmarks.
- Frame rate and performance monitoring.
- A graphical application interface.

## 12. References

- [MediaPipe Hand Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Python Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/)

---

**HandTrack — A Computer Vision Project Built with Python.**
