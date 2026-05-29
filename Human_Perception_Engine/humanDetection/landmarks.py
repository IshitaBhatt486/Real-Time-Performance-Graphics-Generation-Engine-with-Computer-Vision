LANDMARK_NAMES = {

    0:"nose",

    1:"left_eye_inner",
    2:"left_eye",
    3:"left_eye_outer",

    4:"right_eye_inner",
    5:"right_eye",
    6:"right_eye_outer",

    7:"left_ear",
    8:"right_ear",

    11:"left_shoulder",
    12:"right_shoulder",

    13:"left_elbow",
    14:"right_elbow",

    15:"left_wrist",
    16:"right_wrist",

    23:"left_hip",
    24:"right_hip",

    25:"left_knee",
    26:"right_knee",

    27:"left_ankle",
    28:"right_ankle"

}

POSE_CONNECTIONS = [

    # HEAD

    ("nose","left_eye"),
    ("nose","right_eye"),

    ("left_eye","left_ear"),
    ("right_eye","right_ear"),

    # TORSO

    ("left_shoulder","right_shoulder"),

    ("left_shoulder","left_hip"),
    ("right_shoulder","right_hip"),

    ("left_hip","right_hip"),

    # LEFT ARM

    ("left_shoulder","left_elbow"),
    ("left_elbow","left_wrist"),

    # RIGHT ARM

    ("right_shoulder","right_elbow"),
    ("right_elbow","right_wrist"),

    # LEFT LEG

    ("left_hip","left_knee"),
    ("left_knee","left_ankle"),

    # RIGHT LEG

    ("right_hip","right_knee"),
    ("right_knee","right_ankle")

]

def normalized_to_pixel(
    self,
    x,
    y,
    width,
    height
):

    px = int(x * width)

    py = int(y * height)

    return px, py


