# HUMAN PERCEPTION MODULE

Converts raw camera input frames into a stable and structured representation of human motion

---

**Input**: Raw camera feed

**Output**: 
```
{
    body_skeleton,
    hand_landmarks,
    face_landmarks (optional),
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
Pose Estimation
   ↓
Tracking + Smoothing
   ↓
Motion Representation Output
```
---

Steps:
- Video capture: a stable video pipeline that continuously captures camera frames and converts them into NumPy arrays
- Image preprocessing: (resizing, color conversion, normalization, noise reduction, brightness correction) Takes the raw camera frames and cleans them up for better pose detection
