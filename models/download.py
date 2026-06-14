from ultralytics import YOLO

print("Starting YOLOv8 download...")

# YOLo download on this line, it will automatically download the model and save it to the specified path
model = YOLO("models/yolov8n.pt")

print("YOLOv8 model downloaded and saved successfully!")