#Application to run both streamlit, and fastapi
import threading
import uvicorn
import os
import sys

def run_fastapi():
    """Function to run the FastAPI application."""
    uvicorn.run("main:app", host="127.0.0.1", port=8001, log_level="info")  # Change to 8001 if needed

def run_streamlit():
    """Function to run the Streamlit application."""
    os.system("streamlit run streamlit_app.py")

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
