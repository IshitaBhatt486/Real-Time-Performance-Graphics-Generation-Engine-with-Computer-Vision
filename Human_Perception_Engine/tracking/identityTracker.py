import math

import cv2

class IdentityTracker:

    def __init__(self):
        self.next_id = 0
        self.tracked_people = {}

    def compute_centroid(
        self,
        pose_data
    ):

        xs = []
        ys = []

        for joint in pose_data:

            xs.append(
                pose_data[joint]["x"]
            )

            ys.append(
                pose_data[joint]["y"]
            )

        if len(xs) == 0:
            return None

        centroid_x = int(sum(xs)/len(xs))
        centroid_y = int(sum(ys)/len(ys))

        return (
            centroid_x,
            centroid_y
        )
    
    def register_person(
        self,
        centroid
    ):

        person_id = self.next_id

        self.tracked_people[
            person_id
        ] = {

            "centroid":centroid

        }

        self.next_id += 1

        return person_id
    
    def distance(self, p1, p2):
        return math.sqrt(
            (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        )

    def update(
        self,
        people_pose_data
    ):

        tracked_output = {}

        for pose_data in people_pose_data:

            centroid = self.compute_centroid(
                pose_data
            )

            if centroid is None:
                continue

            matched_id = None

            min_distance = float("inf")

            for person_id in self.tracked_people:

                old_centroid = self.tracked_people[
                    person_id
                ]["centroid"]

                dist = self.distance(
                    centroid,
                    old_centroid
                )

                if dist < min_distance:
                    min_distance = dist
                    matched_id = person_id

            if matched_id is None or min_distance > 100:
                matched_id = self.register_person(
                    centroid
                )

            self.tracked_people[
                matched_id
            ]["centroid"] = centroid

            tracked_output[
                matched_id
            ] = {
                "pose":pose_data,
                "centroid":centroid
            }

        return tracked_output
    
    def draw_ids(
        self,
        frame,
        tracked_people
    ):

        for person_id in tracked_people:

            centroid = tracked_people[
                person_id
            ]["centroid"]

            cv2.putText(
                frame,
                f"Person {person_id}",
                centroid,
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,255),
                2
            )

        return frame