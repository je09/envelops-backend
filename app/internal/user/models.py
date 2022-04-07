from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CHAR
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    sex = Column(Integer)  # 1 – f, 2 - m, 0 - not specified
    country = Column(Integer)
    city = Column(String)
    occupation = Column(String)
