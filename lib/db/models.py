from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base()



class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    username = Column(String(16))
    
    scoreboards = relationship("Scoreboard", back_populates="players")
    escapes = relationship("Escape", back_populates="players")

    def __repr__(self):
        return f"id: {self.id}, username: {self.username}"



class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    body = Column(String)
    answer = Column(String)
    hint = Column(String)
    points = Column(Integer)
    
    roomScoreboards = relationship("Scoreboard", back_populates="rooms")

    def __repr__(self):
        return f"id: {self.id}, A: {self.answer}, Points: {self.points}"
    

class Scoreboard(Base):
    __tablename__ = 'scoreboards'
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    room_id = Column(Integer, ForeignKey("rooms.id"))
    count = Column(Integer)
    total_score = Column(Integer)
    
    players = relationship("Player", back_populates="scoreboards")
    rooms = relationship("Room", back_populates="roomScoreboards")

    def __repr__(self):
        return f"id: {self.id}, Player: {self.player_id}, Room: {self.room_id}, Count: {self.count}, Room Score: {self.total_score}"


class Escape(Base):
    __tablename__='escapes'
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    rooms_complete = Column(Integer)
    score = Column(Integer)
    time = Column(String)

    players = relationship("Player", back_populates="escapes")

    def __repr__(self):
        return f"id: {self.id}, player: {self.player_id}, rooms completed: {self.rooms_complete}, score: {self.score}, time: {self.time}"
    