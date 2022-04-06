from fastapi import APIRouter, Depends, status
from typing import List, Optional
from app.internal.group import schemas
from app.internal.group import crud
from app.dependencies import get_db
from app.internal.utils import vk_params_parse

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_group(group: schemas.Group, db=Depends(get_db)):
    crud.create_group(db, group, vk_params_parse(group.params))
    return {
        "result": "ok",
        "error": "",
    }


@router.get("/{client_id}", response_model=List[schemas.ResponseGroup], status_code=status.HTTP_200_OK)
def get_groups(client_id: int, db=Depends(get_db)):
    return crud.read_groups(db, client_id)


@router.delete("/", status_code=status.HTTP_202_ACCEPTED)
def delete_group(group: schemas.Group, db=Depends(get_db)):
    crud.delete_group(db, group, vk_params_parse(group.params))


@router.post("/scenario", status_code=status.HTTP_201_CREATED)
def create_scenario(scenario: schemas.Scenario, db=Depends(get_db)):
    crud.create_scenario(db, scenario)
    return {
        "result": "ok",
        "error": "",
    }


@router.get("/scenario/{group_id}", status_code=status.HTTP_200_OK)
def get_scenarios(group_id: int, db=Depends(get_db)):
    return crud.read_scenarios(db, group_id)
