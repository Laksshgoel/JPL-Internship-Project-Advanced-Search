import requests
import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO
import cloudinary
import cloudinary.uploader
cloudinary.config(
    cloud_name="dm7qsyh77",
    api_key="456649282336662",
    api_secret="5u2wGhQ0lDJb8IUyndhXQB9_toM"
)
model = YOLO("yolov8n.pt")

def object_detection_section():
    st.subheader("📷 Image Object Detection")

    uploaded_file = st.file_uploader("🖼️ Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        img_array = np.array(image)
        results = model.predict(img_array)
        result = results[0]

        object_classes =  ['car', 'truck', 'bus', 'motorcycle', 'bicycle', 'person', 'aeroplane', 'train', 'boat',
'traffic light',
'fire hydrant',
'stop sign',
'parking meter',
'bench',
'bird',
'cat',
'dog',
'horse',
'sheep',
'cow',
'elephant',
'bear',
'zebra',
'giraffe',
'backpack',
'umbrella',
'handbag',
'tie',
'suitcase',
'frisbee',
'skis',
'snowboard',
'sports ball',
'kite',
'baseball bat',
'baseball glove',
'skateboard',
'surfboard',
'tennis racket',
'bottle',
'wine glass',
'cup',
'fork',
'knife',
'spoon',
'bowl',
'banana',
'apple',
'sandwich',
'orange',
'broccoli',
'carrot',
'hot dog',
'pizza',
'donut',
'cake',
'chair',
'sofa',
'pottedplant',
'bed',
'diningtable',
'toilet',
'tvmonitor',
'laptop',
'mouse',
'remote',
'keyboard',
'cell phone',
'microwave',
'oven',
'toaster',
'sink',
'refrigerator',
'book',
'clock',
'vase',
'scissors',
'teddy bear',
'hair drier',
'toothbrush']

        detected_objects = []
        annotated_img = result.plot()

        for box in result.boxes:
            cls = result.names[int(box.cls[0])]
            if cls in object_classes:
                detected_objects.append(cls)

        st.image(annotated_img, caption="📍 Detected Objects", use_container_width=True)

        if detected_objects:
            st.success("✅ Objects Found:")
            for obj in sorted(set(detected_objects)):
                st.markdown(f"- {obj}")

             # Upload image to Cloudinary
            uploaded_file.seek(0)
            try:
                upload_result = cloudinary.uploader.upload(uploaded_file, folder="object_detection_uploads")
                image_url = upload_result["secure_url"]
                print(image_url)
                # Save detected objects and image_url to backend
                response = requests.post(
                    "http://127.0.0.1:8001/save_detections",
                    json={
                        "image_url": image_url,
                        "object_names": list(set(detected_objects))
                    }
                )
                if response.status_code == 200:
                    st.info("Detected objects and image URL saved to database.")
                else:
                    st.error("Failed to save detected objects.")
            except Exception as e:
                st.error(f"Error saving to database: {e}")
        else:
            st.warning("No known objects detected.")