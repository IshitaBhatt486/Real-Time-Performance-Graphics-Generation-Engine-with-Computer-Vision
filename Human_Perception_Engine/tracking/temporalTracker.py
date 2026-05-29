class TemporalTracker:

    def __init__(self):
        self.previous_pose = None
        self.alpha = 0.7
        self.history = {}

    def smoothing(
        self,
        current_pose
    ):

        if self.previous_pose is None:

            self.previous_pose = current_pose

            for joint in current_pose:

                self.history[joint] = [
                    (
                        current_pose[joint]["x"],
                        current_pose[joint]["y"]
                    )
                ]

            return current_pose

        smoothed_pose = {}

        for joint in current_pose:

            if joint not in self.previous_pose:
                self.previous_pose[joint] = current_pose[joint]

            if joint not in self.history:
                self.history[joint] = []

            if len(self.history[joint]) > 50:
                self.history[joint].pop(0)

            old_x = self.previous_pose[joint]["x"]
            old_y = self.previous_pose[joint]["y"]

            current_x = current_pose[joint]["x"]
            current_y = current_pose[joint]["y"]

            smooth_x = int(
                self.alpha * current_x + (1 - self.alpha) * old_x
            )

            smooth_y = int(
                self.alpha * current_y + (1 - self.alpha) * old_y
            )

            smoothed_pose[joint] = {

                "x": smooth_x,
                "y": smooth_y,

                "z": current_pose[joint]["z"],

                "visibility":
                current_pose[joint]["visibility"]

            }

            self.history[joint].append(
                (smooth_x, smooth_y)
            )

        for joint in smoothed_pose:
            self.previous_pose[joint] = smoothed_pose[joint]

        return smoothed_pose