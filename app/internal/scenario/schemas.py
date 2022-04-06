from pydantic import BaseModel
from typing import Optional, List


class ResponseScenario(BaseModel):
    scenario_id: int


class RequestScenario(BaseModel):
    data: str
    texts: List[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True
