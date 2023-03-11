# Std Lib
from base64 import b64decode
import json

# From Library
from fastapi import Request, Body
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


# Imports from files
from .helper_classes import CustomHTTPException


def get_private_key():
    with open("private_key.pem") as file:
        return file.read()


from .config import Config


def decrypt_rsa(encrypted_data):
    if not encrypted_data:
        return {}
    data = b64decode(encrypted_data)
    key = RSA.import_key(Config.ASSYM_PRIVATE_KEY)
    cipher = PKCS1_v1_5.new(key)
    message = cipher.decrypt(data, None)
    return message


def handle_decoding_error(_: Request, exc: CustomHTTPException):
    return JSONResponse(exc.detail, status_code=exc.status_code)


async def decrypt_json(data: str = Body()):
    # print(data)
    return json.loads(decrypt_rsa(data).decode("utf-8"))


def validate_request(ModelCls, request_body):
    try:
        ModelCls(**request_body)
    except ValidationError as e:
        raise CustomHTTPException(status_code=400, detail=e.json())
