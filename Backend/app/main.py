import os

# From Library
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

# Imports From File
from app.core.utils.helper_classes import CustomHTTPException
from app.core.utils.helpers import decrypt_rsa, handle_decoding_error
from app.routers.auth import router as auth_router

app = FastAPI(debug=os.getenv("APP_ENV") == "development")

app.add_exception_handler(CustomHTTPException, handle_decoding_error)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/api")


@app.get("/", name="Health", tags=["Health"])
@app.get("/health", name="Health", tags=["Health"])
def health():
    return "working"
