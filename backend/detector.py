from ultralytics import YOLO

# 1. FIXED PATH: Points to the models folder where you just downloaded it
model = YOLO("models/yolov8n.pt")

# 2. FIXED PATH: Points to a specific image in your datasets folder
# (Make sure you have an image named 'station.jpg' inside your datasets/ folder!)
results = model("datasets/station.jpg")

person_count = 0

# Loop through everything YOLO detected
for box in results[0].boxes:
    cls = int(box.cls[0])  # Get the class ID

    if cls == 0:  # In YOLO, Class 0 is always a 'person'
        person_count += 1

print("-" * 30)
print("RAKSHAK AI DETECTION REPORT")
print("-" * 30)
print("People detected:", person_count)
print("-" * 30)