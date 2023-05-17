from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Player, Scoreboard, Room

engine = create_engine("sqlite:///escape_app.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# session.query(Player).delete()
# session.query(Scoreboard).delete()


# ned = Player(username="ned")
# joe = Player(username="joe")
# patrob = Player(username="patrob")

# session.add(ned)
# session.add(joe)
# session.add(patrob)

# all_players = session.query(Player).all()
# names = [player.username for player in all_players]

# def find_name(name):
#     if name in names:
#         x = session.query(Player).filter(Player.username == name).first()
#         return x
#     else:
#         return Player(username=name)

# session.commit()






import ipdb; ipdb.set_trace()