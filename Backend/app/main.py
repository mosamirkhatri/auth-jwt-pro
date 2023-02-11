# From Library
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Imports From File
from app.core.utils.helper_classes import CustomHTTPException
from app.core.utils.helpers import handle_decoding_error
from app.routers.auth import router as auth_router

app = FastAPI(exception_handlers={CustomHTTPException: handle_decoding_error})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(auth_router)


@app.get("/")
@app.get("/health")
def health():
    return "working"
