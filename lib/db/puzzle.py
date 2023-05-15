from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
    

puzzle1 = Puzzle(
    name = 'letter pattern',
    points = 1000,
    difficulty = 'easy',
    body = 'M -> N  //  G -> T  //  K -> P  //  C -> ?',
    answer = 'X',
    hint = 'Go back to your ABCs'
)

puzzle2 = Puzzle(
    name = 'Breath Riddle',
    points = 1000,
    difficulty = 'easy',
    body = 'I am light as a feather, and can keep it aloft.  Most of the time I am silnet and soft.  I am with you always in whispers and song.  The strongest of men can\'t hold me for long.',
    answer = 'breath',
    hint = 'I am invisible but can be seen in the cold'
)

# engine = create_engine('sqlite:///game.db', echo=True)
# Base.metadata.create_all(engine)
