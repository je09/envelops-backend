import requests
from sqlalchemy.orm import Session
from app.internal.scenario.crud import read_group_id
from app.internal.group.crud import read_token
from .base import ENDPOINT


def __request(vk_id: int, vk_token: int):
    r = requests.get(
        ENDPOINT.format(method="users.get",
                        params=f"user_ids={vk_id}&fields=sex,country,city,occupation",
                        token=vk_token)
    )

    if r.status_code != 200:
        pass

    return r.json()


def get(db: Session, vk_params: dict, scenario_id: int):
    vk_id = vk_params["vk_user_id"]
    vk_group_id = read_group_id(db, scenario_id)
    vk_token = read_token(db, vk_group_id)

    return __request(vk_id, vk_token)



