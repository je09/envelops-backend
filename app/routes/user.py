from fastapi import APIRouter, Depends, status
from typing import List
from app.internal.user import crud, schemas
from app.dependencies import get_db
from app.internal.utils import vk_params_parse
from app.internal.vk import users

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.RequestUser, db=Depends(get_db)):
    user_info = users.get(db, vk_params_parse(user.params), user.scenario_id)
    user_db = crud.create_user(db, schemas.User(
        scenario_id=user.scenario_id,
        sex=user_info["sex"],
        country={True: user_info["country"]["title"], False: ""}["country" in user_info],
        city={True: user_info["city"]["title"], False: ""}["city" in user_info],
        occupation=user_info["occupation"]["type"] if "occupation" in user_info else ""
    ))

    return {
        "result": "ok",
        "user_id": user_db.id,
        "error": ""
    }


@router.get("/{scenario_id}", status_code=status.HTTP_200_OK)
def get_user(scenario_id: int, db=Depends(get_db)):
    return crud.get_users(db, scenario_id)
