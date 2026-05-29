import cv2
import torch
import numpy as np

from torchvision import models
from torchvision import transforms

class HumanSegmentation:
    def __init__(self):

        self.model = models.segmentation.deeplabv3_mobilenet_v3_large(
            weights="DEFAULT"
        )

        self.model.eval()

        self.transform = transforms.Compose([

            transforms.ToTensor(),

            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )

        ])

        # warming up the model with a dummy input
        dummy = np.zeros(
            (256,256,3),
            dtype=np.uint8
        )

        self.segment(dummy)

    def segment(self, frame):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        frame_resized = cv2.resize(
            rgb_frame,
            (256,256)
        )

        input_tensor = self.transform(
            frame_resized
        )

        input_batch = input_tensor.unsqueeze(0)

        with torch.no_grad():
            output = self.model(
                input_batch
            )["out"][0]

        output_predictions = output.argmax(0)

        segmentation_map = (
            output_predictions
            .cpu()
            .numpy()
            .astype("uint8")
        )

        segmentation_map = cv2.resize(
            segmentation_map,
            (
                frame.shape[1],
                frame.shape[0]
            ),
            interpolation=cv2.INTER_NEAREST
        )

        return segmentation_map
    
    def create_person_mask(
        self,
        segmentation_map
    ):
        person_mask = np.where(segmentation_map == 15, 255, 0).astype("uint8")

        return person_mask.astype("uint8")
    
    def extract_human(
        self,
        frame,
        person_mask
    ):
        isolated = cv2.bitwise_and(
            frame,
            frame,
            mask=person_mask
        )

        return isolated

    def addGaussianBlur(
        self,
        mask
    ):
        blurred = cv2.GaussianBlur(
            mask,
            (11,11),
            0
        )

        return blurred