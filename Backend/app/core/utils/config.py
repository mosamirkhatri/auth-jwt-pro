import os


class Config:
    JWT_SECRET = os.getenv('JWT_SECRET')
    JWT_ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    SAME_SITE_POLICY = "none" if os.getenv("APP_ENV") == "development" else "strict"
