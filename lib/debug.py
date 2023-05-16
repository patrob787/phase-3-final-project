from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Room
import ipdb;

engine = create_engine("sqlite:///escape_app.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
q = session.query(Room.body)
print(q)




ipdb.set_trace()