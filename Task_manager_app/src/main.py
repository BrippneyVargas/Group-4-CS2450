from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.tasks import router
import uvicorn

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)