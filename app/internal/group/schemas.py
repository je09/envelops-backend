from pydantic import BaseModel
from typing import Optional


class GroupParams(BaseModel):
    vk_access_token_settings: Optional[str] = ""
    vk_app_id: int
    vk_are_notifications_enabled: bool
    vk_is_app_user: bool
    vk_is_app_user: str
    vk_platform: str
    vk_user_id: int


class Group(BaseModel):
    group_id: int
    group_token: str
    params: str

