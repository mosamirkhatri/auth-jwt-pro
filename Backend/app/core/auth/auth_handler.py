from datetime import datetime, timedelta, timezone
from typing import List, Literal

# Library
import jwt
from fastapi.responses import JSONResponse

# Import from files
from ..utils.config import Config


def sign_jwt(
    user_id: str, role: str, type: Literal["access", "refresh"] = "access"
) -> str:
    secret_key = Config.JWT_REFRESH_SECRET if type == "refresh" else Config.JWT_SECRET
    payload = {
        "user_id": user_id,
        "aud": role,
        "iat": int(datetime.now(tz=timezone.utc).timestamp()),
        "exp": int(
            (
                datetime.now(tz=timezone.utc)
                + timedelta(
                    minutes=Config.REFRESH_TOKEN_EXPIRE_MINUTES
                    if type == "refresh"
                    else Config.ACCESS_TOKEN_EXPIRE_MINUTES
                )
            ).timestamp()
        ),
    }

    token = jwt.encode(payload, secret_key, algorithm=Config.JWT_ALGORITHM)

    return token


def decode_jwt(
    token: str, aud: List[str], type: Literal["access", "refresh"] = "access"
):
    secret_key = Config.JWT_REFRESH_SECRET if type == "refresh" else Config.JWT_SECRET
    return jwt.decode(token, secret_key, audience=aud, algorithms=Config.JWT_ALGORITHM)


def generate_auth_response(user):
    a_token = sign_jwt(user.get("id"), user.get("role"))
    r_token = sign_jwt(user.get("id"), user.get("role"), type="refresh")

    *access_token, sign = a_token.split(".")
    access_token = ".".join(access_token)

    *refresh_token, r_sign = r_token.split(".")
    refresh_token = ".".join(refresh_token)

    response = JSONResponse(
        content={
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
        }
    )

    response.set_cookie(
        "sign",
        sign,
        httponly=True,
        secure=True,
        samesite=Config.SAME_SITE_POLICY,
        expires=Config.ACCESS_TOKEN_EXPIRE_MINUTES * 60 + 300,
    )

    response.set_cookie(
        "r_sign",
        r_sign,
        httponly=True,
        secure=True,
        samesite=Config.SAME_SITE_POLICY,
        expires=Config.REFRESH_TOKEN_EXPIRE_MINUTES * 60 + 300,
    )

    return response
