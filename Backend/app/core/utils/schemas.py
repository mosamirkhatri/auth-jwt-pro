from typing import Optional
from pydantic import BaseModel


class AdminTest(BaseModel):
    hello: Optional[str]
    world: Optional[str]
    lol: str
