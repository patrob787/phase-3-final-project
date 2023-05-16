from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from player import Player, Base
from scoreboard import Scoreboard
from rooms import Room

class Game:
    def __init__(self):
        self.engine = create_engine('sqlite:///game.db', echo=True)
        self.metadata = MetaData()
        self.questions = Table('questions', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('question', String),
            Column('answer', String),
            Column('hint', String),
            Column('score', Integer)
        )
        Base.metadata.create_all(self.engine)

    def ask_questions(self):
        new_player = input("Enter your name: ")
        print(f'Welcome {new_player}!...................................... begin game')

        Session = sessionmaker(bind=self.engine)
        session = Session()

        # create a new player and scoreboard and link them together
        player1 = Player(username=new_player, score=0, health=100)
        room1 = Room(player=player1, username=player1.username, room1=False, room2=False, room3=False, room4=False, room5=False, room6=False, room7=False, room8=False, room9=False)
        score1 = Scoreboard(player=player1, score=player1.score, username=player1.username, games_completed=0)
        session.add(room1)
        session.add(player1)
        session.add(score1)
        session.commit()

        score = 0
        room_attrs = ['room1', 'room2', 'room3', 'room4', 'room5', 'room6', 'room7', 'room8', 'room9']
        correct_answers = 0
        for i in range(5):
            query = session.query(self.questions).filter(self.questions.c.score > score).order_by(func.random()).limit(1)
            row = query.first()
            if row is None:
                print("No more questions available. Exiting the game.")
                break

            question, answer, hint, question_score = row.question, row.answer, row.hint, row.score

            while correct_answers < 5:
                user_answer = input(question + "\n> ")
                if user_answer.lower() == answer.lower():
                    score += question_score
                    print("\033[32mCorrect! Your score is now", score, "\033[0m")

                    # update the room attribute for the question answered correctly
                    setattr(room1, room_attrs[i], True)
                    session.commit()
                    correct_answers += 1
                    break
                else:
                    player1.health -= 10  # deduct 10 health points for a wrong answer
                    print("\033[31mIncorrect.\033[0m Here's a hint: \033[33m" + hint + "\033[0m")
                    if player1.health >= 70:
                        color = '\033[32m'
                    elif player1.health >= 30:
                        color = '\033[33m'
                    else:
                        color = '\033[31m'
                    print(f"{color}Incorrect! Your health is now {player1.health}\033[0m")

                    # check if player is out of health and end the game if they are
                    if player1.health <= 0:
                        print(f"{new_player} is out of health. Game over.")
                        session.commit()
                        return
                    print("Please try again.")

        # update player and scoreboard objects with new score
        player1.score += score
        score1.score += score
        score1.games_completed += sum([getattr(room1, attr) for attr in room_attrs])
        session.commit()

        print("Your final score is", score)

run_game = Game()
run_game.ask_questions()
