"""
This is the main file to run the FastAPI and Streamlit applications.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import router
import threading
import uvicorn
import os

app = FastAPI(title="Task Manager API")

# Register API routes
app.include_router(router)

# Enabling CORS for frontend (Streamlit). Found it on the internet that it is required.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def run_fastapi():
    """Function to run the FastAPI application."""
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")  # Change to 8001 if needed

def run_streamlit():
    """Function to run the Streamlit application."""
    os.system("streamlit run ./Task_manager_app/src/TaskManager.py")

if __name__ == "__main__":
    # Create threads for running FastAPI and Streamlit
    fastapi_thread = threading.Thread(target=run_fastapi)
    streamlit_thread = threading.Thread(target=run_streamlit)

    # Start the FastAPI thread
    fastapi_thread.start()

    # Start the Streamlit thread
    streamlit_thread.start()

    # Wait for both threads to finish
    fastapi_thread.join()
    streamlit_thread.join()
