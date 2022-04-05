from sqlalchemy.orm import Session
from app.internal.group.schemas import Group


def create_group(db: Session, group: Group):
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

