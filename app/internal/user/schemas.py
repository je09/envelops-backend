from pydantic import BaseModel
from typing import Optional


class RequestUser(BaseModel):
    scenario_id: int
    params: Optional[str]


class User(BaseModel):
    scenario_id: int
    sex: int
    country: int
    city: str
    occupation: str
