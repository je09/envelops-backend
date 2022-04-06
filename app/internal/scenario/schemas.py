from pydantic import BaseModel
from typing import Optional, List


class ResponseCookies(BaseModel):
    scenario_id: int


class RequestCookies(BaseModel):
    data: str
    texts: List[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True