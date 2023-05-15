from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    scoreboards = relationship("Scoreboard", back_populates="player")
    rooms = relationship("Room", back_populates="player")
    username = Column(String(16))
    health = Column(Integer, default=100)
    score = Column(Integer, default=0)

