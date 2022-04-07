from pydantic import BaseModel
from typing import Optional, List, Dict


class ResponseScenario(BaseModel):
    scenario_id: int


class DefineScenario(ResponseScenario):
    picture_link: str
    data: List[str]


class RequestScenario(BaseModel):
    data: str
    texts: str

    class Config:  # to convert non dict obj to json
        orm_mode = True


class ScenarioData(BaseModel):
    id: int


class Scenario(BaseModel):
    name: Optional[str]
    type: int
    group_id: int
    params: Optional[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True
