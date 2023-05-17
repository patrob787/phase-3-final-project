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

    puzzle1 = Room(
        body="M -> N  //  G -> T  //  K -> P  //  C -> ?",
        answer="X",
        hint="Go back to your ABCs",
        points=1000,
    )

    puzzle2 = Room(
        body="I am light as a feather, and can keep it aloft.  Most of the time I am silent and soft.  I am with you always in whispers and song.  The strongest of men can't hold me for long.",
        answer="breath",
        hint="I am invisible but can be seen in the cold",
        points=1000,
    )

    puzzle3 = Room(
        body="What Is The Next Letter In The Progression?  W I T N L I T ?",
        answer="P",
        hint="The answer is the title.",
        points=1000,
    )

    puzzle4 = Room(
        body="""These nine numbers spell a word:
                1 5 5 8 9 6 8 7
                
                Can you decode the word using only this clue?
                9 1 9 6 8 9 6 8 = NONSENSE""",
        answer="offenses",
        hint="What are the first letters in the numbers?",
        points=1000,
    )

    puzzle5 = Room(
        body="Two times 10 like a basket, holds six of us within its casket / but 9 can only make room for four / if muddled by your addition, you must abandon that mission / and contemplate this one admission, 5 also holds within it four but 8 holds five of us and not one more!  What are we?",
        answer="letters",
        hint="What can you count other than numbers?  Why are some numbers spelled out?",
        points=1000,
    )

    puzzle6 = Room(
        body="Find the missing number: 05, 08, 13, 21, ??, 55",
        answer="34",
        hint="Fibonacci says Hello World!",
        points=1000,
    )

    puzzle7 = Room(
        body="""1, 4, 7, 11, 15, 19, 21
                These numbers are bound in a progression.  When written, it may come into view.  The rule they follow is in question.  What number is next?  No math will do!
            """,
        answer="24",
        hint="Try writing down the numbers as words.",
        points=1000,
    )


    session.add(puzzle1)
    session.add(puzzle2)
    session.add(puzzle3)
    session.add(puzzle4)
    session.add(puzzle5)
    session.add(puzzle6)
    # session.add(puzzle7)
    session.commit()