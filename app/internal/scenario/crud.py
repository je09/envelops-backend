from sqlalchemy.orm import Session
from app.internal.scenario.models import Scenario


def create_scenario(db: Session, scenario):
    db_scenario = Scenario(group_id=scenario.group_id, name=scenario.name, type=scenario.type)
    db.add(db_scenario)
    db.commit()
    db.refresh(db_scenario)
    return db_scenario


def read_scenarios(db: Session, group_id: int):
    return db.query(Scenario).where(Scenario.group_id == group_id).all()

