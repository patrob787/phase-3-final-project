from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Player, Scoreboard, Room, Puzzle,  Base


new_player = input("Enter your name: ") # get the player's name from input stores in variable

print(f'Welcome {new_player}!...................................... begin game')

engine = create_engine("sqlite:///game.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# create a new player and scoreboard and link them together
player1 = Player(username=new_player, score=400, keys=300)
room1 = Room(player=player1,username=player1.username, room1=True, room2=False, room3=False, room4=False, room5=False, room6=False, room7=False, room8=False, room9=False)
score1 = Scoreboard(player=player1, score=player1.score, username=player1.username, games_completed=3)
session.add(room1)
session.add(player1)
session.add(score1)
session.commit()

# query the scoreboards and join them with the players
scoreboards = session.query(Scoreboard).join(Player).all()
for scoreboard in scoreboards:
    print(scoreboard.player.username, scoreboard.score, scoreboard.username)
