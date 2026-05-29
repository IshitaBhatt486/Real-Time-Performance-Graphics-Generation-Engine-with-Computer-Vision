# HUMAN PERCEPTION MODULE

Computes where the body is and converts raw camera input frames into a stable and structured representation of human motion

---

**Input**: Raw camera feed

**Output**: 
```
motion_data = {

   "skeleton":joint_coordinates,
   "body_orientation":orientation,
   "segmentation_mask":mask,
   "tracked_history":history,
   "timestamps":time_data

}
```
---

### Basic Architecture:

```
Camera
   ↓
Raw Frame
   ↓
Image Pre-processing
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
Identity Tracking
   ↓
Persistent Performer Objects
   ↓
Semantic Segmentation
   ↓
Person Extraction
   ↓
Mask smoothing
   ↓
Rendering
   ↓
Display
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
- Identity tracking system
- Human Segmentation to get a full body silhouette
- Sends output to Motion Representation Module

---

### Tools used:
- Python
- MediaPipe
- DeepLabV3

### Python Libraries:
- NumPy
- OpenCV
- PyTorch