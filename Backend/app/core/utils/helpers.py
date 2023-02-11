# From Library
from fastapi import Request
from fastapi.responses import JSONResponse

# Imports from files
from .helper_classes import CustomHTTPException


def handle_decoding_error(_: Request, exc: CustomHTTPException):
    return JSONResponse(exc.detail, status_code=exc.status_code)
