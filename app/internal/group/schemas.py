from pydantic import BaseModel
from typing import Optional


class Group(BaseModel):
    group_id: int
    group_token: str
    params: str


class ResponseGroup(BaseModel):
    group_id: int

    class Config:  # to convert non dict obj to json
        orm_mode = True


class Scenario(BaseModel):
    name: str
    type: int
    group_id: int
    params: Optional[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True
