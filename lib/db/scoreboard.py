from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from player import Base

class Scoreboard(Base):
    __tablename__ = 'scoreboards'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="scoreboards")
    username = Column(String)
    score = Column(Integer)
    games_completed = Column(Integer)

