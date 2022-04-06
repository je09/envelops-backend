from fastapi import APIRouter, Depends, status
from typing import List, Optional
from app.internal.scenario import schemas
from app.internal.scenario import crud
from app.dependencies import get_db
from app.internal.utils import vk_params_parse


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_scenario(scenario: schemas.ResponseScenario, db=Depends(get_db)):
    crud.create_scenario(db, scenario)
    return {
        "result": "ok",
        "error": "",
    }


@router.get("/{group_id}", status_code=status.HTTP_200_OK)
def get_scenarios(group_id: int, db=Depends(get_db)):
    return crud.read_scenarios(db, group_id)
