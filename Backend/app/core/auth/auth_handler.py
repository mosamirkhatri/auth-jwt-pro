from datetime import datetime, timedelta, timezone
from typing import List

# Library
import jwt

# Import from files
from ..utils.config import Config


def sign_jwt(user_id: str, role: str) -> str:
    payload = {
        "user_id": user_id,
        "aud": role,
        "iat": int(datetime.now(tz=timezone.utc).timestamp()),
        "exp": int(
            (
                datetime.now(tz=timezone.utc)
                + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
            ).timestamp()
        ),
    }

    token = jwt.encode(payload, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)

    return token


def decode_jwt(token: str, aud: List[str]):
    return jwt.decode(
        token, Config.JWT_SECRET, audience=aud, algorithms=Config.JWT_ALGORITHM
    )
