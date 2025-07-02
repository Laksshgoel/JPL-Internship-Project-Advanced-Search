from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import HTTPException
# --- MongoDB Connection ---
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"  # Change if using MongoDB Atlas/cloud
client = MongoClient(MONGO_URI)
db = client["InternProject"]  # Replace with your database name
detections_collection = db["QueryBasedObjectDetection"]  # Replace with your collection name

# --- FastAPI App ---
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WordRequest(BaseModel):
    word: str

@app.post("/echo")
def echo_word(request: WordRequest):
    return {"received_word": request.word}

# Example endpoint to save a detection to MongoDB
class DetectionBatch(BaseModel):
    image_url: str
    object_names: List[str]

@app.post("/save_detections")
def save_detections(batch: DetectionBatch):
    try:
        doc = {"image_url": batch.image_url, "object_names": batch.object_names}
        detections_collection.insert_one(doc)
        return {"message": "Detections saved!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": "This is your item."}