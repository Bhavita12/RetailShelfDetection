# inference.py
# Script to run inference using a trained YOLOv8 model on test images
# Author: Seela Bhavita

from ultralytics import YOLO
import os

# Path to the trained model
MODEL_PATH = "/weights/best.pt"

# Path to test images
SOURCE_DIR = "/retail_data/test_images"

# Output directory
OUTPUT_DIR = "/RetailShelfDetection/sample_outputs"

# Load the trained model
model = YOLO(MODEL_PATH)

# Run inference
results = model.predict(
    source=SOURCE_DIR,
    save=True,
    save_txt=True,
    conf=0.25,
    imgsz=640,
    project=OUTPUT_DIR,
    name="results",
    exist_ok=True
)

print(f"Inference complete! Results saved to: {os.path.join(OUTPUT_DIR, 'results')}")
