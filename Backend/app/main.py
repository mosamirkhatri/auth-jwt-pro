import os

# From Library
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

# Imports From File
from app.core.utils.helper_classes import CustomHTTPException
from app.core.utils.helpers import handle_decoding_error
from app.routers.auth import router as auth_router

app = FastAPI(debug=os.getenv("APP_ENV") == "development")

app.add_exception_handler(CustomHTTPException, handle_decoding_error)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/api")


@app.get("/", name="Health", tags=["Health"])
@app.get("/health", name="Health", tags=["Health"])
def health():
    return "working"
