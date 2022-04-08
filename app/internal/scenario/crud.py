from sqlalchemy.orm import Session
from app.internal.scenario.models import Scenario, ScenarioTemplate


def create_scenario(db: Session, scenario):
    db_scenario = Scenario(group_id=scenario.group_id, type=scenario.type)
    db.add(db_scenario)
    db.commit()
    db.refresh(db_scenario)
    return db_scenario


def read_scenarios(db: Session, group_id: int):
    return db.query(Scenario).where(Scenario.group_id == group_id).all()


def read_scenario(db: Session, scenario_id: int):
    return db.query(Scenario).where(Scenario.id == scenario_id).first()


def read_group_id(db: Session, scenario_id: int):
    return db.query(Scenario).where(Scenario.id == scenario_id).first().group_id


def update_scenario(db: Session, scenario):
    stmnt = db.query(Scenario).filter(Scenario.id == scenario.scenario_id)\
        .update({"data": scenario.data, "picture_link": scenario.picture_link})
    db.commit()
    return stmnt


# TODO: THIS IS FUCKING SHITCODE
def create_cookies(db: Session):
    db_cookies = ScenarioTemplate(type=1, name="Cookies", description="Test!")
    if db.query(ScenarioTemplate).where(ScenarioTemplate.type == 1).first():
        return
    db.add(db_cookies)
    db.commit()
    db.refresh(db_cookies)
    return db_cookies
