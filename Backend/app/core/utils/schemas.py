from typing import Optional
from pydantic import BaseModel


class AdminTest(BaseModel):
    hello: Optional[str]
    world: Optional[str]


class Login(BaseModel):
    username: str
    password: str
