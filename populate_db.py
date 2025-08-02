import os
import base64
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["InternProject"]
collection = db["QueryBasedObjectDetection"]

# Path to your dataset
dataset_path = "101_ObjectCategories"

# Traverse folders
for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    if os.path.isdir(folder_path):
        object_name = folder.lower()
        for filename in os.listdir(folder_path):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode("utf-8")
                    doc = {
                        "objects": [object_name],
                        "image_data": encoded
                    }
                    collection.insert_one(doc)

print("✅ All images uploaded to MongoDB")
