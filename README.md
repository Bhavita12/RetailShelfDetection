README.md

--> Retail Shelf Object Detection

->  Project Overview

This project focuses on building a multi-class object detection model to identify and localize products on cluttered retail shelves. The goal is to accurately detect:

- Cereal Boxes
- Soda Cans
- Water Bottles

The model is trained using the YOLOv8 framework, fine-tuned on a custom dataset containing real-world challenges like occlusion, multiple object classes, and dense product arrangements.

----------------------------------------------

->  Dataset Description

The dataset was organized with the following structure:

retail_data/
├── images/
│ ├── train/ # Training images (.jpg)
│ └── val/ # Validation images (.jpg)
├── labels/
│ ├── train/ # YOLO annotations (.txt)
│ └── val/
└── data.yaml # Dataset configuration file


- Classes: 11 in total, focus of this submission is on **class 9 (Cereal Box)**
- Format: YOLO (bounding boxes in text files)
- Each class has 50+ annotated images
- Includes cluttered and partially occluded products to simulate real shelf conditions

-----------------------------------------------

->  Model Training

- **Model**: YOLOv8n (Ultralytics)
- **Transfer Learning**: Pre-trained weights (yolov8n.pt) used and fine-tuned
- **Epochs**: 50
- **Framework**: PyTorch with Ultralytics YOLOv8
- **Platform**: Google Colab + Google Drive

->  Command Used:

```bash
!yolo task=detect mode=train \
  model=yolov8n.pt \
  data=/retail_data/data.yaml \
  epochs=50 \
  imgsz=640

Model weights are saved at:

RetailShelfDetection/weights/best.pt

->  Inference

To run inference on new shelf images:

from ultralytics import YOLO
model = YOLO('RetailShelfDetection/weights/best.pt')
results = model('path_to_test_image.jpg', save=True, conf=0.25)

~Annotated images are saved with bounding boxes & labels
~Batch inference results saved to:

  RetailShelfDetection/sample_outputs/results/

->  Evaluation Metrics

Metric	         Value
mAP@0.5	         66.4%
mAP@0.5:0.95	 54.7%
Precision	 50.6%
Recall	         75.8%

->  Class-wise AP@0.5:

Class	         AP (%)
Coke	         71.1
Pepsi	         61.4
Sprite	         36.5 
1-5L_Pet	 81.9
270_Sparking	 80.9

->  Observations

~High recall indicates the model finds most objects correctly.
~Precision is lower due to clutter and visual similarity (e.g., Sprite vs. Pepsi).
~Performance is best on larger bottles like 1-5L_Pet.
~Occlusion and lighting variations were present in training data.

->  Directory Structure

RetailShelfDetection/
├── retail_data/                  # images and labels
├── weights/                      # best.pt
├── inference.py                  # inference script
├── evaluation_report.md          # detailed evaluation
├── sample_outputs/               # annotated test outputs
│   └── results/
└── README.md                     # project overview

->  Acknowledgments

Thanks to Ultralytics, Open Images, and Roboflow for tools and resources used in this project.

This work was done as part of the Computer Vision Internship Project: Object Detection in Retail Shelf Images.