from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    # scoreboards = relationship("Scoreboard", back_populates="player")
    # rooms = relationship("Room", back_populates="player")
    username = Column(String(16))
    health = Column(Integer, default=100)
    score = Column(Integer, default=0)



class Puzzle(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    points = Column(Integer)
    difficulty = Column(Integer)
    body = Column(String)
    answer = Column(String)
    hint = Column(String)

    def __repr__(self):
        return f"id: {self.id}, {self.name}, difficulty level: {self.level}, Points: {self.points}"
    


class Room(Base):
    __tablename__='rooms'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="rooms")
    username = Column(String(16))
    room1 = Column(Boolean, default=None)
    room2 = Column(Boolean, default=None)
    room3 = Column(Boolean, default=None)
    room4 = Column(Boolean, default=None)
    room5 = Column(Boolean, default=None)
    room6 = Column(Boolean, default=None)
    room7 = Column(Boolean, default=None)
    room8 = Column(Boolean, default=None)
    room9 = Column(Boolean, default=None)



class Scoreboard(Base):
    __tablename__ = 'scoreboards'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="scoreboards")
    username = Column(String)
    score = Column(Integer)
    games_completed = Column(Integer)