from pydantic import BaseModel
from typing import Optional, List


class Leak(BaseModel):
    email: str
    password: str
    date: Optional[str]
    sources: Optional[List[str]]


class APIReponse(BaseModel):
    success: bool
    results: Optional[List[Leak]]
