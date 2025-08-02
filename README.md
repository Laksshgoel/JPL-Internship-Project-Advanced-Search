# Jio Internship Project – Object Detection App

This repository contains the code developed during my 2-month internship (June–July 2025) at **Jio AI Cloud** under the mentorship of **Mr. Shashank Upadhyay**. The project focuses on building an **object detection and search system** that tags objects in images and enables object-based image retrieval.

## 🚀 Project Overview

The goal was to build a full-stack application for:

- Detecting and tagging objects in images using **YOLOv8**
- Storing image metadata in **MongoDB**
- Serving APIs with **FastAPI**
- Creating a simple UI using **Streamlit**
- Hosting image files securely using **Cloudinary**
- Enabling object-based search functionality

## 🛠️ Tech Stack

| Layer         | Tools/Frameworks             |
|--------------|------------------------------|
| Detection     | YOLOv8 (Ultralytics)         |
| Backend       | FastAPI, Pydantic            |
| Frontend      | Streamlit                    |
| Database      | MongoDB                      |
| Storage       | Cloudinary                   |
| Deployment    | Local                        |

## 📁 Directory Structure

project-root/
├── backend/ # FastAPI backend and APIs
├── frontend/ # Streamlit frontend
├── models/ # YOLOv8 model and inference code
├── populate_db.py # Script to populate MongoDB
├── requirements.txt # Python dependencies
└── README.md # This file


## 📷 Features

- Upload images and auto-detect objects
- Store object tags in MongoDB
- Search images by object name
- Interactive UI using Streamlit
- Scalable architecture with modular components


## 👤 Author

**Lakssh Goel**  
B.Tech (SE), Delhi Technological University  
Intern @ Jio AI Cloud (June–July 2025)  
Email: laksshgoelbosco@gmail.com

**Siddhant Tomar**  
B.Tech (IT), National Institute of Technology Raipur  
Intern @ Jio AI Cloud (June–July 2025)  
Email: siddhanttomar2003@gmail.com

## 📜 License

This project is proprietary and was developed for Jio Platforms Ltd. All rights reserved.<<<<<<< HEAD
# My Streamlit and FastAPI Application

This project is a web application that utilizes FastAPI for the backend and Streamlit for the frontend. The application is designed to demonstrate how to create a full-stack application using these two powerful frameworks.

## Getting Started

To get started with this project, follow the instructions below.

### Prerequisites

Make sure you have Python 3.7 or higher installed on your machine.

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-streamlit-fastapi-app
   ```

2. Set up the backend:
   - Navigate to the `backend` directory:
     ```
     cd backend
     ```
   - Install the backend dependencies:
     ```
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory:
     ```
     cd ../frontend
     ```
   - Install the frontend dependencies:
     ```
     pip install -r requirements.txt
     ```

### Running the Application

1. Start the FastAPI backend:
   - Navigate to the `backend` directory and run:
     ```
     uvicorn app:app --reload
     ```

2. Start the Streamlit frontend:
   - Navigate to the `frontend` directory and run:
     ```
     streamlit run app.py
     ```

3. Start the MongoDB Compass
   
4. Sign in to Cloudinary to get cloud_name, api_key & api_secret_key. 

### Usage

Once both the backend and frontend are running, you can access the Streamlit application in your web browser at `http://localhost:8501`. The frontend will interact with the FastAPI backend to fetch and display data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
=======
# JPL-Internship-Project-Advanced-Search
AI-powered object detection and retrieval system using YOLOv8. Includes Streamlit frontend, FastAPI backend, MongoDB database, and Cloudinary for image storage. Supports object-based search, image tagging, and fuzzy query correction using LanguageTool.
>>>>>>> b82094caeaa04ed8c5cc8e68a55f971c10095fb3
