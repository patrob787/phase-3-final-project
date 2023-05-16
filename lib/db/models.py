from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    username = Column(String(16))
    scoreboards = relationship("Scoreboard", back_populates="players")

    def __repr__(self):
        return f"id: {self.id}, username: {self.username}"


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    body = Column(String)
    answer = Column(String)
    hint = Column(String)
    points = Column(Integer)
    roomScoreboards = relationship("Scoreboard", back_populates="rooms")

    def __repr__(self):
        return f"id: {self.id}, A: {self.answer}, Points: {self.points}"


class Scoreboard(Base):
    __tablename__ = "scoreboards"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    players = relationship("Player", back_populates="scoreboards")
    room_id = Column(Integer, ForeignKey("rooms.id"))
    rooms = relationship("Room", back_populates="roomScoreboards")
    score = Column(Integer)

    def __repr__(self):
        return f"id: {self.id}, Player: {self.player_id}, Room: {self.room_id}, Room Score: {self.score}"


# class Escape(Base):
#     __tablename__='escapes'
#     id = Column(Integer, primary_key=True)
#     player_id = Column(Integer, ForeignKey('players.id'))
#     player = relationship("Player", back_populates="rooms")
#     username = Column(String(16))
#     room1 = Column(Boolean, default=None)
#     room2 = Column(Boolean, default=None)
#     room3 = Column(Boolean, default=None)
#     room4 = Column(Boolean, default=None)
#     room5 = Column(Boolean, default=None)
#     room6 = Column(Boolean, default=None)
#     room7 = Column(Boolean, default=None)
#     room8 = Column(Boolean, default=None)
#     room9 = Column(Boolean, default=None)
