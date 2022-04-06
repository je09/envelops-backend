from fastapi import APIRouter, Depends, status
from typing import List
from app.internal.user import crud, schemas
from app.dependencies import get_db
from app.internal.utils import vk_params_parse

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User, db=Depends(get_db)):
    crud.create_user(db, user, vk_params_parse(user.params))

    return {
        "result": "ok",
        "error": ""
    }


@router.get("/{group_id}", status_code=status.HTTP_200_OK)
def get_user(group_id: int, db=Depends(get_db)):
    pass
