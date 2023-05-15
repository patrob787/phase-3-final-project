from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    scoreboards = relationship("Scoreboard", back_populates="player")
    username = Column(String(50))
    health = Column(Integer, default=100)
    money = Column(Integer)
    score = Column(Integer)

    def __repr__(self):
        return f"Player(id={self.id}, username='{self.username}', health={self.health}, score={self.score}, money={self.money})"
