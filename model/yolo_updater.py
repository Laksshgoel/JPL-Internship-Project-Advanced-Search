from pymongo import MongoClient
from ultralytics import YOLO
import base64
import io
from PIL import Image
import numpy as np

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["InternProject"]
collection = db["QueryBasedObjectDetection"]

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # adjust path if needed

def decode_image(base64_str):
    img_bytes = base64.b64decode(base64_str)
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    return np.array(image)

# Loop through all images in the collection
updated = 0
for doc in collection.find():
    image_np = decode_image(doc["image_data"])
    results = model(image_np)

    detected_labels = set()
    for result in results:
        detected_labels.update(result.names[i] for i in result.boxes.cls.tolist())

    # Update the document with new detected objects
    collection.update_one(
        {"_id": doc["_id"]},
        {"$set": {"objects": list(detected_labels)}}
    )
    updated += 1
    print(f"Updated '{doc['filename']}' with: {list(detected_labels)}")

print(f"\n✅ Completed. Updated {updated} documents.")
