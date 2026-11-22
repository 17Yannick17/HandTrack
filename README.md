# HandTrack

**Real-Time Hand Tracking and Finger Counting Using Python, OpenCV and MediaPipe**

HandTrack is a computer vision application that detects and tracks a human hand in real time using a webcam. It identifies 21 hand landmarks and uses geometric analysis to count raised fingers.

The project explores computer vision, hand pose estimation, geometric algorithms and real-time video processing.

## 1. Features

### Implemented

- Real-time webcam capture using OpenCV.
- Hand detection using MediaPipe Hand Landmarker.
- Visualization of 21 hand landmarks and their connections.
- Real-time tracking of hand movements.
- Detection status displayed on screen.
- Safe webcam initialization and resource cleanup.

### In Development

- Finger counting from 0 to 5.
- Individual finger state detection.
- Automated unit tests for finger counting.

### Planned

- Recognition of predefined gestures:
  - Closed Fist
  - Open Palm
  - Victory
- Gesture-based visual feedback.
- Improved gesture stability and recognition accuracy.

## 2. Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Webcam capture and image processing |
| MediaPipe | Hand landmark detection and tracking |
| NumPy | Numerical operations |
| pytest | Automated unit testing |
| Git & GitHub | Version control and project management |
| PyCharm | Development environment |

The application uses a pretrained MediaPipe Hand Landmarker model. No custom machine learning model training is required.

## 3. Project Architecture

```text
HandTrack/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── hand_tracker.py
│   └── finger_counter.py
│
├── tests/
│   └── test_finger_counter.py
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

**Main components:**

- `main.py`: manages webcam capture, application execution and video display.
- `hand_tracker.py`: detects hand landmarks using MediaPipe and draws them on video frames.
- `finger_counter.py`: analyzes hand landmark geometry to determine the number of raised fingers.
- `test_finger_counter.py`: contains automated tests for finger counting.
- `models/`: stores the pretrained MediaPipe model.
- `docs/`: contains the project requirements, technical documentation and test results.

The `.venv` directory and pretrained model file are excluded from Git version control.

## 4. Installation

### Prerequisites

- Python 3.14 (development environment) or a compatible Python version.
- Git.
- A working webcam.
- An operating system and Python environment supported by the required dependencies.

### Step 1 — Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/HandTrack.git
cd HandTrack
```

Replace `YOUR_USERNAME` with the repository owner's GitHub username.

### Step 2 — Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment on Windows (CMD):

```cmd
.venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4 — Download the MediaPipe model

Create the `models` directory if it does not exist:

```cmd
mkdir models
```

Download the pretrained Hand Landmarker model on Windows:

```cmd
curl.exe -L --fail "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task" -o "models\hand_landmarker.task"
```

The model must be saved at:

`models/hand_landmarker.task`

For more information, see [Model Documentation](models/README.md).

## 5. Usage

Start the application from the project root directory:

```bash
python -m src.main
```

A window opens and displays the webcam stream.

**Instructions:**

1. Place your hand in front of the webcam.
2. Wait for the hand landmarks to appear.
3. Move your hand and observe the tracking.
4. During finger-counting development, test different finger positions.
5. Press `Q` to close the application.

The application processes webcam images locally.

## 6. How It Works

HandTrack follows a real-time computer vision processing pipeline:

```text
Webcam
   |
   v
Frame Capture (OpenCV)
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
Geometric Analysis
   |
   v
Finger Counting (0–5)
   |
   v
Real-Time Visualization
```

### Hand Landmark Detection

MediaPipe detects 21 reference points corresponding to the wrist and finger joints.

These landmarks provide normalized coordinates describing the position of the hand.

### Finger Counting

The finger-counting module analyzes the positions of the landmarks using geometric calculations, including:

- Joint angles.
- Distances between landmarks.
- Relationships between fingertips and the hand.

Each finger is classified as either raised or folded.

The application counts the raised fingers to produce a value between 0 and 5.

The approach is based on geometric heuristics and may be affected by hand rotation, occlusion and lighting conditions.

## 7. Testing

HandTrack uses automated unit tests and manual webcam validation.

### Automated Tests

Run the test suite from the project root:

```bash
python -m pytest tests/ -v
```

The tests are designed to validate:

- Finger counting from 0 to 5.
- Individual finger states.
- Mirrored landmark configurations.
- Invalid landmark data.
- Invalid frame dimensions.

### Manual Tests

Manual validation includes:

- Webcam initialization.
- Hand landmark detection.
- Hand movement tracking.
- Finger-count accuracy.
- Behavior when no hand is visible.
- Proper application shutdown.

Test execution results are recorded in [Test Report](docs/test_report.md).

## 8. Project Management

HandTrack follows a lightweight, structured software development process.

Development tasks are managed using GitHub Issues and a Kanban board.

Each feature is developed in a dedicated Git branch, tested and integrated through a Pull Request.

### Development Roadmap

| Issue | Feature | Status |
|---|---|---|
| #1 | Webcam capture | Completed |
| #2 | Hand landmark detection | Completed |
| #3 | Finger counting | In progress |
| #4 | Gesture recognition | Planned |
| #5 | Visual feedback and actions | Planned |
| #6 | Testing and final documentation | Planned |

The project uses descriptive Git commits and feature branches to maintain a traceable development history.

## 9. Documentation

Additional project documentation is available:

- [Project Requirements](docs/requirements.md)
- [Software Architecture](docs/architecture.md)
- [Test Report](docs/test_report.md)
- [Model Documentation](models/README.md)

## 10. Known Limitations

- Only one hand is processed at a time.
- Detection accuracy depends on webcam image quality.
- Finger-counting accuracy can decrease under strong hand rotations or occlusions.
- Geometric thresholds may require calibration.
- Advanced gesture recognition is not yet implemented.

## 11. Future Improvements

Possible enhancements include:

- Multi-hand tracking.
- Additional gesture recognition.
- Gesture-controlled presentation slides.
- Gesture-based system volume control.
- Improved recognition using 3D landmark information.
- Performance monitoring and FPS display.

## 12. References

- [MediaPipe Hand Landmarker Documentation](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Python Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/)

---

**HandTrack — A Computer Vision Project Built with Python.**