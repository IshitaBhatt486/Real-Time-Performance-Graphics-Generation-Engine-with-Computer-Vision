# Motion Representation Module

Computes how the body is moving. Converts raw positional data into mathematical representation.

---

### Inputs: (from Human Perception Engine)

motion_data = {

   "skeleton":joint_coordinates,
   "body_orientation":orientation,
   "segmentation_mask":mask,
   "tracked_history":history,
   "timestamps":time_data

}

### Outputs:

For every joint:

```
{
    "position": (x,y),
    "velocity": (vx,vy),
    "speed": value,
    "acceleration": (ax,ay),
    "joint_angle": theta,
    "trajectory": [...],
    "history": [...]
}
```

---

# Architecture:

