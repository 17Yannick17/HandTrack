
# HandTrack

**Real-Time Hand Tracking and Gesture Recognition Using Python**

![Python Tests](https://github.com/17Yannick17/HandTrack/actions/workflows/python-tests.yml/badge.svg)

HandTrack is a real-time computer vision application that detects and tracks a human hand using a webcam, counts raised fingers, recognizes predefined hand gestures, and triggers interactive visual feedback.

The application combines MediaPipe hand landmark detection, custom geometric algorithms, temporal gesture stabilization, and OpenCV-based visualization.

The project was developed following a structured software engineering workflow, including requirements analysis, modular implementation, automated testing, documentation, GitHub Issues, and Pull Requests.

## 1. Demo

**[Watch the HandTrack Demonstration](assets/demo.mp4)**

The demonstration showcases:

- Real-time hand landmark tracking.
- Finger counting from 0 to 5.
- Recognition of Fist, Open Palm, and Victory gestures.
- Interactive visual feedback.
- Action event counting.

## 2. Features

### Real-Time Hand Tracking

- Webcam capture using OpenCV.
- Detection of 21 hand landmarks using MediaPipe.
- Visualization of hand landmarks and their connections.
- Continuous tracking of hand movements.
- Detection status displayed on screen.

### Finger Counting

- Count raised fingers from 0 to 5.
- Determine the individual state of each finger.
- Analyze hand geometry using joint angles and distances.
- Support left and right hands independently.

### Gesture Recognition

HandTrack recognizes three predefined gestures:

| Gesture | Finger Configuration |
|---|---|
| Fist | All fingers folded |
| Open Palm | All fingers raised |
| Victory | Index and middle raised, other fingers folded |
| Unknown | Any other configuration |

Gesture recognition uses custom classification rules based on the detected finger states.

### Temporal Stabilization

A gesture must be detected in four consecutive frames before being confirmed.

This reduces short-term classification flickering and improves visual stability.

The gesture state is reset when no hand is detected.

### Interactive Visual Feedback

Each recognized gesture triggers a visual action:

| Gesture | Action | Color |
|---|---|---|
| Fist | ALERT | Red |
| Open Palm | READY | Green |
| Victory | SUCCESS | Blue |
| Unknown | WAITING | Neutral |
| No Hand | NO HAND | Neutral |

The application also provides:

- Color-coded interface borders.
- A visual action status panel.
- A counter of triggered actions.
- A temporary notification for new actions.

Actions are triggered when the confirmed gesture changes, not on every video frame.

## 3. Technologies

| Technology | Purpose |
|---|---|
| Python 3.14 | Programming language |
| OpenCV | Webcam capture and image processing |
| MediaPipe | Hand landmark detection |
| NumPy | Numerical operations |
| pytest | Automated unit testing |
| Git | Version control |
| GitHub | Source hosting and issue tracking |
| GitHub Actions | Continuous integration |
| PyCharm | Development environment |

HandTrack uses a pretrained MediaPipe Hand Landmarker model.

No custom machine learning model is trained. The finger-counting and gesture-classification logic is implemented using geometric algorithms.

## 4. Project Architecture

HandTrack follows a modular architecture designed to separate video acquisition, perception, classification, and visual interaction.

### Project Structure

```text
HandTrack/
|
|-- .github/
|   `-- workflows/
|       `-- python-tests.yml
|
|-- src/
|   |-- __init__.py
|   |-- main.py
|   |-- hand_tracker.py
|   |-- finger_counter.py
|   |-- gesture_detector.py
|   `-- gesture_actions.py
|
|-- tests/
|   |-- test_finger_counter.py
|   |-- test_gesture_detector.py
|   `-- test_gesture_actions.py
|
|-- models/
|   |-- README.md
|   `-- hand_landmarker.task
|
|-- docs/
|   |-- requirements.md
|   |-- architecture.md
|   `-- test_report.md
|
|-- assets/
|   `-- demo.mp4
|
|-- .gitignore
|-- requirements.txt
|-- CHANGELOG.md
`-- README.md
```

The virtual environment and downloaded model file are excluded from version control.

### Main Modules

**main.py**

- Initializes and manages the webcam.
- Coordinates the processing pipeline.
- Displays the annotated video.
- Handles application shutdown.

**hand_tracker.py**

- Loads the pretrained MediaPipe model.
- Detects hand landmarks.
- Draws landmarks and connections.

**finger_counter.py**

- Calculates geometric relationships between landmarks.
- Determines which fingers are raised.
- Counts the number of raised fingers.

**gesture_detector.py**

- Classifies gestures using finger states.
- Handles unknown gestures.
- Stabilizes predictions across consecutive frames.

**gesture_actions.py**

- Maps recognized gestures to visual actions.
- Tracks gesture transitions.
- Displays interactive visual feedback.
- Maintains the action counter.

### Processing Pipeline

```text
Webcam
   |
   v
Video Capture (OpenCV)
   |
   v
Frame Preprocessing (BGR to RGB)
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
Interactive Video Display
```

For more information, see [Software Architecture](docs/architecture.md).

## 5. Installation

### Prerequisites

- Python 3.14.
- Git.
- A working webcam.
- Windows with webcam access enabled.

The project was developed and validated locally using PyCharm on Windows.

Other environments may work if compatible versions of the dependencies are available, but they are not part of the documented validation environment.

### Step 1 — Clone the Repository

```cmd
git clone https://github.com/17Yannick17/HandTrack.git
cd HandTrack
```

### Step 2 — Create a Virtual Environment

```cmd
python -m venv .venv
```

Activate the virtual environment using Windows CMD:

```cmd
.venv\Scripts\activate
```

### Step 3 — Install Dependencies

```cmd
python -m pip install -r requirements.txt
```

Verify the installed dependencies:

```cmd
python -m pip check
```

### Step 4 — Download the MediaPipe Model

Create the models directory if needed:

```cmd
mkdir models
```

Download the pretrained Hand Landmarker model:

```cmd
curl.exe -L --fail "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task" -o "models\hand_landmarker.task"
```

The model must be saved at:

`models/hand_landmarker.task`

See [Model Documentation](models/README.md) for additional details.

### Step 5 — Start HandTrack

```cmd
python -m src.main
```

The webcam window should open automatically.

## 6. Usage

1. Position one hand in front of the webcam.
2. Wait for MediaPipe to detect the hand landmarks.
3. Raise different fingers to test finger counting.
4. Make a Fist, Open Palm, or Victory gesture.
5. Observe the recognized gesture and corresponding action.
6. Change gestures to trigger new visual events.
7. Press **Q** to close the application.

### Example Behavior

**Fist**

The application recognizes a closed fist and activates the red ALERT state.

**Open Palm**

The application recognizes an open hand and activates the green READY state.

**Victory**

The application recognizes the index and middle fingers raised and activates the blue SUCCESS state.

**Unknown**

The application displays a neutral WAITING state when a gesture is not recognized.

**No Hand**

The active gesture and visual feedback are reset when the hand disappears.

## 7. Algorithms

### Hand Landmark Detection

MediaPipe detects 21 hand landmarks and returns their normalized coordinates.

The landmarks correspond to the wrist and finger joints.

### Finger Counting

The finger-counting algorithm uses:

- Joint angles.
- Distances between landmarks.
- Finger extension conditions.
- Palm-relative measurements.

Each finger is classified as raised or folded.

The final count is calculated from the five finger states.

### Gesture Classification

Gesture recognition is based on predefined combinations of finger states.

The algorithm distinguishes Fist, Open Palm, Victory, and Unknown.

### Temporal Stabilization

A gesture must be recognized for four consecutive frames before confirmation.

This reduces sudden changes caused by temporary detection errors.

### Action Event Management

Visual actions are activated only when the confirmed gesture changes to a recognized gesture.

Holding the same gesture does not repeatedly increase the action counter.

## 8. Testing and Validation

HandTrack uses automated unit tests and manual integration testing.

### Automated Tests

Run the complete test suite:

```cmd
python -m pytest tests/ -v
```

The automated tests cover:

- Finger counting from 0 to 5.
- Individual finger states.
- Mirrored landmark configurations.
- Invalid landmark data.
- Gesture classification.
- Temporal stabilization.
- Gesture transitions.
- Action event management.
- Prevention of repeated actions.
- Visual feedback rendering.

### Manual Integration Tests

Manual testing verifies:

- Webcam initialization and shutdown.
- Hand landmark tracking.
- Finger-counting behavior.
- Gesture recognition.
- Interactive visual responses.
- Action counter behavior.
- Unknown and no-hand states.
- Application restart.

### Continuous Integration

GitHub Actions automatically runs the Python test suite on pushes and Pull Requests targeting the main branch.

The workflow installs dependencies, checks Python syntax, verifies dependencies, and executes pytest.

The CI workflow does not require a webcam because the automated tests use simulated hand landmark data.

Actual test execution results are documented in the [Test Report](docs/test_report.md).

## 9. Software Development Process

HandTrack was developed using a lightweight, structured software development lifecycle.

### Planning

The functional requirements and acceptance criteria were defined before implementation.

### Task Management

GitHub Issues and a Kanban board were used to plan and track development tasks.

### Version Control

Each feature was implemented on a dedicated Git branch.

Git commits describe the changes introduced during development.

### Code Integration

Pull Requests were used to review and integrate feature branches into the main branch.

### Verification

Automated tests and manual checks were performed throughout development.

### Documentation

Requirements, architecture decisions, test results, and installation instructions were documented progressively.

### Development Milestones

| Issue | Delivered Feature |
|---|---|
| #1 | Webcam capture |
| #2 | Hand landmark detection |
| #3 | Finger counting |
| #4 | Gesture recognition |
| #5 | Visual feedback and actions |
| #6 | Final validation, documentation and release |

## 10. Documentation

Additional project documentation:

- [Project Requirements](docs/requirements.md)
- [Software Architecture](docs/architecture.md)
- [Test Report](docs/test_report.md)
- [Model Documentation](models/README.md)
- [Changelog](CHANGELOG.md)

## 11. Known Limitations

- Only one hand is processed at a time.
- Detection accuracy depends on lighting and camera quality.
- Strong rotations and occlusions can cause errors.
- Finger counting uses 2D geometric heuristics.
- Gesture recognition depends on finger-state accuracy.
- Temporal stabilization introduces a short delay.
- Visual actions do not control external applications.
- The action counter resets when the application restarts.

## 12. Future Improvements

Potential future developments include:

- Multi-hand tracking.
- Additional gesture classes.
- Gesture-controlled presentation slides.
- Gesture-based system volume control.
- Recognition using 3D hand landmark geometry.
- Performance monitoring and FPS measurement.
- More robust gesture classification using machine learning.
- A dedicated graphical user interface.

## 13. References

- [MediaPipe Hand Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Python Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**HandTrack — Real-Time Computer Vision and Gesture-Based Interaction with Python.**
