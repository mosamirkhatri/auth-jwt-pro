import os
from .helpers import get_private_key


class Config:
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_REFRESH_SECRET = os.getenv("JWT_REFRESH_SECRET")
    JWT_ALGORITHM = "HS256"
    CIPHER_KEY = os.getenv("CIPHER_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES = 6 * 60
    REFRESH_TOKEN_EXPIRE_MINUTES = 15 * 24 * 60
    SAME_SITE_POLICY = "none" if os.getenv("APP_ENV") == "development" else "strict"
    ASSYM_PRIVATE_KEY = get_private_key()
