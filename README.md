# Human Detection and landmark extraction System

- extracts landmarks
- creates a skeletal structure
- stable movement

---

# Architecture:

Camera
   ↓
Human Perception Model
   ↓
Motion Representation Module
   ↓
Output

---

### Tools used:
- Python
- MediaPipe
- DeepLabV3

### Python Libraries:
- NumPy
- OpenCV
- PyTorch

---

# To run:
Run the following commands in the terminal:
```

pip install numpy
pip install opencv-python
pip install mediapipe
pip install torch torchvision

```
---

# Key bugs fixed:
- preserve state and handle detection failure
- replaced DeepLabV3's ResNet101 with mobileNetV3(Reason: speed)

---
This is an ongoing project
# The vision: A Real-Time Performance Graphics Generation Engine
    A low-latency computer vision system that observes and interprets human movement in creative performances and continuously feeds that data into a procedural graphics engine to create real-time visual effects

##  Features:
    - Allows for multiple performers
    - Produces graphics for performance in real-time based on the performer's movements
    - reduced latency
    - parallize operations for increased speed