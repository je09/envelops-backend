from sqlalchemy.orm import Session
from app.internal.user.models import User


def create_user(db: Session, user, params: dict):
    db_user = User(user.id, user.sex, user.country, user.city, user.occupation)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, group_id: int):
    return db.query(User).filter(User)
