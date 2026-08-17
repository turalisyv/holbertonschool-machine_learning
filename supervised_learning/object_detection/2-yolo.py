#!/usr/bin/env python3
"""Script to initialize YOLOv3"""
import tensorflow.keras as K
import numpy as np


class Yolo():
    """Class YOLOv3"""

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """
        Method init for Yolov3

        Args:
            model_path: path to where a Darknet Keras model is stored
            classes_path: path to where the list of class names used for
                          the Darknet model can be found
            class_t: the box score threshold for the initial filtering step
            nms_t: the IOU threshold for non-max suppression
            anchors: the anchor boxes
        """
        self.model = K.models.load_model(model_path)
        with open(classes_path, 'r') as f:
            self.class_names = [line.strip() for line in f]
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    def sigmoid(self, x):
        """Sigmoid function"""
        return 1 / (1 + np.exp(-x))

    def process_outputs(self, outputs, image_size):
        """
        Process Darknet model outputs.

        Args:
            outputs: list of numpy.ndarrays containing predictions
            image_size: numpy.ndarray containing original image size

        Returns:
            tuple: boxes, box_confidences, box_class_probs
        """
        boxes = [pred[:, :, :, 0:4].copy() for pred in outputs]

        input_w = self.model.input.shape[1]
        input_h = self.model.input.shape[2]

        for i, output in enumerate(outputs):
            grid_h, grid_w, anchor_boxes = output.shape[:3]

            for cy in range(grid_h):
                for cx in range(grid_w):
                    tx = output[cy, cx, :, 0]
                    ty = output[cy, cx, :, 1]
                    tw = output[cy, cx, :, 2]
                    th = output[cy, cx, :, 3]

                    bx = (self.sigmoid(tx) + cx) / grid_w
                    by = (self.sigmoid(ty) + cy) / grid_h

                    anchor_w = self.anchors[i, :, 0]
                    anchor_h = self.anchors[i, :, 1]

                    bw = (np.exp(tw) * anchor_w) / input_w
                    bh = (np.exp(th) * anchor_h) / input_h

                    x1 = (bx - (bw / 2)) * image_size[1]
                    y1 = (by - (bh / 2)) * image_size[0]
                    x2 = (bx + (bw / 2)) * image_size[1]
                    y2 = (by + (bh / 2)) * image_size[0]

                    boxes[i][cy, cx, :, 0] = x1
                    boxes[i][cy, cx, :, 1] = y1
                    boxes[i][cy, cx, :, 2] = x2
                    boxes[i][cy, cx, :, 3] = y2

        box_confidences = []
        box_class_probs = []

        for output in outputs:
            box_confidences.append(self.sigmoid(output[:, :, :, 4:5]))
            box_class_probs.append(self.sigmoid(output[:, :, :, 5:]))

        return boxes, box_confidences, box_class_probs

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        """
        Filter boxes based on class scores.

        Args:
            boxes: list of numpy.ndarrays containing processed boxes
            box_confidences: list of numpy.ndarrays containing confidences
            box_class_probs: list of numpy.ndarrays containing class probs

        Returns:
            tuple: filtered_boxes, box_classes, box_scores
        """
        filtered_boxes = []
        box_classes = []
        box_scores = []

        for i, box in enumerate(boxes):
            scores = box_confidences[i] * box_class_probs[i]
            classes = np.argmax(scores, axis=-1)
            class_scores = np.max(scores, axis=-1)
            mask = class_scores >= self.class_t

            filtered_boxes.append(box[mask])
            box_classes.append(classes[mask])
            box_scores.append(class_scores[mask])

        filtered_boxes = np.concatenate(filtered_boxes, axis=0)
        box_classes = np.concatenate(box_classes, axis=0)
        box_scores = np.concatenate(box_scores, axis=0)

        return filtered_boxes, box_classes, box_scores
