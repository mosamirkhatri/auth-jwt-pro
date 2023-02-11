from typing import List

# Library
from fastapi import Cookie, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

# Imports from files
from .auth_handler import decode_jwt
from ..utils.helper_classes import CustomHTTPException

security = HTTPBearer()


class LoginRequired:
    def __init__(self, aud: List[str]):
        self.aud = aud

    def __call__(
        self,
        credentials: HTTPAuthorizationCredentials = Depends(security),
        sign: str = Cookie(None),
    ):
        token = (
            credentials.credentials + "." + sign
            if sign is not None
            else credentials.credentials
        )

        try:
            current_user = decode_jwt(token, self.aud)
        except jwt.DecodeError:
            raise CustomHTTPException(
                detail={"success": False, "message": "Failed to decode token"},
                status_code=401,
            )
        except jwt.ExpiredSignatureError:
            raise CustomHTTPException(
                detail={"success": False, "message": "Token Expired"},
                status_code=401,
            )
        except jwt.InvalidAudienceError:
            raise CustomHTTPException(
                detail={"success": False, "message": "Access denied"},
                status_code=403,
            )
        except jwt.InvalidIssuedAtError:
            raise CustomHTTPException(
                detail={"success": False, "message": "Token can be used in future"},
                status_code=403,
            )
        except jwt.InvalidTokenError:
            raise CustomHTTPException(
                detail={"success": False, "message": "Invalid token"},
                status_code=403,
            )
        except Exception:
            raise CustomHTTPException(
                detail={"success": False, "message": "Token not provided or invalid"},
                status_code=400,
            )
        return current_user
