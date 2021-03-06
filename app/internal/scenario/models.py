from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR, JSON
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship
from app.database import Base


class ScenarioTemplate(Base):
    __tablename__ = 'templates'

    type = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)


class Scenario(Base):
    __tablename__ = 'scneario'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer)
    type = Column(Integer)
    picture_link = Column(String)
    data = Column(JSON)
