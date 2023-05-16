from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from player import Base

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
