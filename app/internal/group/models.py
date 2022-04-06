from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer)
    token = Column(String)
    creator_id = Column(Integer)


class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer)
    name = Column(String)
    type = Column(Integer)
