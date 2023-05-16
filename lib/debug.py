from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Player, Scoreboard, Room

engine = create_engine("sqlite:///escape_app.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


session.query(Player).delete()
session.query(Scoreboard).delete()

session.commit()






import ipdb; ipdb.set_trace()