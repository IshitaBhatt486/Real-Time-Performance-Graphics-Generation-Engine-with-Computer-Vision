# HUMAN PERCEPTION MODULE

Converts raw camera input frames into a stable and structured representation of human motion

---

**Input**: Raw camera feed

**Output**: 
```
{
    body_skeleton,
    hand_landmarks,
    face_landmarks,
    body_orientation,
    tracked_motion_history,
    segmented_human_region
}
```
---

### Basic Architecture:

```
Camera
   ↓
Raw Frame
   ↓
Image Preprocessing
   ↓
Processed frame
   ↓
Human Detection
   ↓
Bounding boxes
   ↓
Landmarks extraction
   ↓
Temporal Tracking
   ↓
State Prediction
   ↓
Correction
   ↓
Stable motion representation
   ↓
Motion Representation Output
```
---

Steps:
---
- Video capture: a stable video pipeline that continuously captures camera frames and converts them into NumPy arrays
- Image preprocessing: (resizing, color conversion, normalization, noise reduction, brightness correction) Takes the raw camera frames and cleans them up for better pose detection
- Detect and locate humans in the frame
- Extract skeletal landmarks
- Draws the skeletal structure
- Temporal tracking and smoothing using weighted average (used moving average earlier)

---

### Tools used:
- Python
- MediaPipe

### Python Libraries:
- NumPy
- OpenCV