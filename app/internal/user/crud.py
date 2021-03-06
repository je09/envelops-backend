from sqlalchemy.orm import Session
from app.internal.user.models import User


def create_user(db: Session, user):
    db_user = User()
    db_user.sex = user.sex
    db_user.country = user.country
    db_user.city = user.city
    db_user.occupation = user.occupation
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, group_id: int):
    return db.query(User).filter(User)


def get_users(db: Session, scenario_id: int):
    return db.query(User).where(User.scenario_id == scenario_id).all()
