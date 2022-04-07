from sqlalchemy.orm import Session
from app.internal.user.models import User


def create_user(db: Session, user):
    db_user = User(user.id, user.sex, user.country, user.city, user.occupation)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, group_id: int):
    return db.query(User).filter(User)


def get_users(db: Session, scenario_id: int):
    return db.query(User).where(User.scenario_id == scenario_id).all()
