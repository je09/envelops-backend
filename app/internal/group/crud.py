from sqlalchemy.orm import Session
from app.internal.group.models import Group, Scenario


def create_group(db: Session, group, params: dict):
    db_group = Group(group_id=group.group_id, token=group.group_token, creator_id=params["vk_user_id"])
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def read_groups(db: Session, creator_id: int):
    return db.query(Group).filter(Group.creator_id == creator_id).all()


def delete_group(db: Session, group, params: dict):
    return db.delete(Group).where(Group.creator_id == params["vk_user_id"] and Group.group_id == group.group_id)


def create_scenario(db: Session, scenario):
    db_scenario = Scenario(group_id=scenario.group_id, name=scenario.name, type=scenario.type)
    db.add(db_scenario)
    db.commit()
    db.refresh(db_scenario)
    return db_scenario


def read_scenarios(db: Session, group_id: int):
    return db.query(Scenario).where(Scenario.group_id == group_id).all()
