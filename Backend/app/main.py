import os

# From Library
from fastapi import FastAPI, Request, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

# Imports From File
from app.core.utils.helper_classes import CustomHTTPException, DecryptionMiddleware
from app.core.utils.helpers import decrypt_rsa, handle_decoding_error
from app.routers.auth import router as auth_router


async def decrypt(data: str = Body()):
    print(data)
    return decrypt_rsa(data)


app = FastAPI(
    debug=os.getenv("APP_ENV") == "development"  # , dependencies=[Depends(decrypt)]
)

app.add_exception_handler(CustomHTTPException, handle_decoding_error)
from starlette.types import Message

# app.add_middleware(DecryptionMiddleware)


async def set_body(request: Request, body: bytes):
    async def receive() -> Message:
        return {"type": "http.request", "body": body}

    request._receive = receive


async def get_body(request: Request) -> bytes:
    body = await request.body()
    await set_body(request, body)
    return body


# app.add_middleware(DecryptionMiddleware)
# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     encrypted_data = await get_body(request)
#     if encrypted_data := encrypted_data.decode("utf-8"):
#         decrypted_data = decrypt_rsa(encrypted_data)
#         print(decrypted_data)
#         await set_body(request, decrypted_data)
#     response = await call_next(request)
#     return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


app.include_router(auth_router)


@app.get("/", name="Health", tags=["Health"])
@app.get("/health", name="Health", tags=["Health"])
def health():
    return "working"
