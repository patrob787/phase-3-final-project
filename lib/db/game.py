from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from player import Player, Base
from scoreboard import Scoreboard


engine = create_engine('sqlite:///game.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# create a new player and scoreboard and link them together
player1 = Player(username='cake', score=400, money=300)
score1 = Scoreboard(player=player1, score=player1.score, username=player1.username)
session.add(player1)
session.add(score1)
session.commit()

# query the scoreboards and join them with the players
scoreboards = session.query(Scoreboard).join(Player).all()
for scoreboard in scoreboards:
    print(scoreboard.player.username, scoreboard.score, scoreboard.username)
