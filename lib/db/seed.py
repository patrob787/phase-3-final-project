from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Room, Player, Scoreboard, Base


if __name__ == "__main__":
    engine = create_engine("sqlite:///escape_app.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    session.query(Player).delete()
    session.query(Scoreboard).delete()
    session.query(Room).delete()

    # puzzle1 = Room(
    #     body="M -> N  //  G -> T  //  K -> P  //  C -> ?",
    #     answer="X",
    #     hint="Go back to your ABCs",
    #     points=1000,
    # )

    # puzzle2 = Room(
    #     body="I am light as a feather, and can keep it aloft.  Most of the time I am silent and soft.  I am with you always in whispers and song.  The strongest of men can't hold me for long.",
    #     answer="breath",
    #     hint="I am invisible but can be seen in the cold",
    #     points=1000,
    # )



    # session.add(puzzle1)
    # session.add(puzzle2)
    session.commit()