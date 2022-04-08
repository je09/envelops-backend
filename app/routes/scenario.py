from fastapi import APIRouter, Depends, status
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from app.internal.scenario import schemas
from app.internal.scenario import crud
from app.dependencies import get_db
from app.internal.utils import vk_params_parse


router = APIRouter()


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_scenario(scenario: schemas.Scenario, db=Depends(get_db)):
    crud.create_cookies(db)
    db_scenario = crud.create_scenario(db, scenario)
    return {
        "result": "ok",
        "data": {
            "id": db_scenario.id,
        },
        "error": "",
    }


@router.get("/get/{group_id}", status_code=status.HTTP_200_OK)
def get_scenarios(group_id: int, db=Depends(get_db)):
    return crud.read_scenarios(db, group_id)


@router.get("/read/{scenario_id}", status_code=status.HTTP_200_OK)
def get_scenario(scenario_id: int, db=Depends(get_db)):
    return crud.read_scenario(db, scenario_id)


@router.post("/define")
def define_scenario(scenario: schemas.DefineScenario, db=Depends(get_db)):
    scenario_id = crud.update_scenario(db, scenario)
    return {
        "result": "ok",
        "data": {
            "id": scenario_id,
        },
        "error": "",
    }
