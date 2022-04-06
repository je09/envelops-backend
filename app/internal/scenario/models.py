from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR, JSON
from sqlalchemy.orm import relationship
from app.database import Base


class Scenarios(Base):
    __tablename__ = 'scneario'

    id = Column(Integer, primary_key=True)
    scenario_id = Column(Integer)
    type = Column(Integer)
    data = Column(JSON)
