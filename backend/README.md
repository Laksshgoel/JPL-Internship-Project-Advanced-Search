# Backend README.md

# My Streamlit and FastAPI Application - Backend

This is the backend component of the My Streamlit and FastAPI application. It is built using FastAPI, a modern web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/my-streamlit-fastapi-app.git
   cd my-streamlit-fastapi-app/backend
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI backend, execute the following command:

```
uvicorn app:app --reload
```

This will start the server at `http://127.0.0.1:8000`. The `--reload` flag enables auto-reload, so the server will restart upon code changes.

## API Documentation

Once the server is running, you can access the interactive API documentation at:

```
http://127.0.0.1:8000/docs
```

## Usage Examples

You can interact with the API using tools like `curl`, Postman, or directly from the frontend application. Make sure to check the API endpoints defined in `app.py` for available routes and their usage.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.