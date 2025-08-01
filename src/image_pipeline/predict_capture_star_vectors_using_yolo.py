from ultralytics import YOLO
from pathlib import Path

# Load your trained model (use the path to the trained weights)
model = YOLO('runs/detect/custom_yolo/weights/best.pt')

# Path to image(s) you want to detect stars in
# Can be a single image or a folder of images
image_path = str(Path(__file__).parent / 'starfield.png')

# Run prediction (inference)
results = model.predict(source=image_path, save=True, conf=0.02, device="mps", show=True, line_width=2)

# `save=True` will save output images with bounding boxes
# `show=True` will open a window to display them (optional)
