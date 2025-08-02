from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson import ObjectId
from fastapi.responses import JSONResponse
import base64

app = FastAPI()

# CORS (allow Streamlit to access FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["InternProject"]
collection = db["QueryBasedObjectDetection"]

@app.get("/search")
def search_images(query: str):
    results = collection.find({"objects": query})
    images = []
    for r in results:
        img_data = r["image_data"]  # base64 encoded string
        images.append(img_data)
    return JSONResponse(content={"images": images})
