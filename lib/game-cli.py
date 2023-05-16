from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Player, Scoreboard, Room,  Base
# from sqlalchemy.sql.expression import func


if __name__ == '__main__':

    input("Hello...and welcome to...")

    print("""
    
        _        _        _       _____  _       _____                                          _        _        _    
     /\| |/\  /\| |/\  /\| |/\   / ____|| |     |_   _|                                      /\| |/\  /\| |/\  /\| |/\ 
     \ ` ' /  \ ` ' /  \ ` ' /  | |     | |       | | ______  ___   ___  __ _  _ __    ___   \ ` ' /  \ ` ' /  \ ` ' / 
    |_     _||_     _||_     _| | |     | |       | ||______|/ __| / __|/ _` || '_ \  / _ \ |_     _||_     _||_     _|
     / , . \  / , . \  / , . \  | |____ | |____  _| |_       \__ \| (__| (_| || |_) ||  __/  / , . \  / , . \  / , . \ 
     \/|_|\/  \/|_|\/  \/|_|\/   \_____||______||_____|      |___/ \___|\__,_|| .__/  \___|  \/|_|\/  \/|_|\/  \/|_|\/ 
                                                                              | |                                      
                                                                              |_|                                      

    """)
    input("press enter to continue...if you dare.")

    new_player = input("Enter your name: ") # get the player's name from input stores in variable

    print(f'Welcome {new_player}!  Are you ready to begin?')
    start_game = input('Y/n ?: ')
    
    if start_game.lower() == 'y':
        
        # current_player = Player(name=new_player)
        # current_player.score = 0
        # current_player.attempts = 5
        # current_player.hints = 3
        

        print(f"{new_player} you have been trapped inside of the CLI.  Your only chance at escaping is to complete a gauntlet of challenges.  There are ?? challenges in total to complete.  You'll have a total of 10 missed-attempts and 3 hints to use at anytime.  If you run out of attempts, the game is lost.  For each room you complete you will recieve points.  For escaping the CLI you will recieve a bonus score!")
        input("Press enter when you are ready to CLI-scape!  Good luck!")
        
        

    else:
        print("Okay...well, goodluck!")

    # engine = create_engine("sqlite:///escape_app.db", echo=True)
    # Base.metadata.create_all(engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()

    # create a new player and scoreboard and link them together
    # player1 = Player(username=new_player, score=0, health=100)
    # room1 = Room(player=player1, username=player1.username, room1=False, room2=False, room3=False, room4=False, room5=False, room6=False, room7=False, room8=False, room9=False)
    # score1 = Scoreboard(player=player1, score=player1.score, username=player1.username, games_completed=0)
    # score = 0


    # session.add(room1)
    # session.add(player1)
    # session.add(score1)
    # session.commit()


    # for i in range(9):
    #     query = session.query(self.questions).filter(self.questions.c.score > score).order_by(func.random()).limit(1)
    #     row = query.first()
    #     if row is None:
    #         print("No more questions available. Exiting the game.")
    #         break

    #     question, answer, hint, question_score = row.question, row.answer, row.hint, row.score
    #     correct_answers = 0

    #     while correct_answers < 5:
    #         user_answer = input(question + "\n> ")
    #         if user_answer.lower() == answer.lower():
    #             score += question_score
    #             print("\033[32mCorrect! Your score is now", score, "\033[0m")
                
    #             # update the room attribute for the question answered correctly
    #             setattr(room1, room_attrs[i], True)
    #             session.commit()
    #             correct_answers += 1
    #             break
    #         else:
    #             player1.health -= 10  # deduct 10 health points for a wrong answer
    #             print("\033[31mIncorrect.\033[0m Here's a hint: \033[33m" + hint + "\033[0m")
    #             if player1.health >= 70:
    #                 color = '\033[32m'
    #             elif player1.health >= 30:
    #                 color = '\033[33m'
    #             else:
    #                 color = '\033[31m'
    #             print(f"{color}Incorrect! Your health is now {player1.health}\033[0m")
    #             # check if player is out of health and end the game if they are
    #             if player1.health <= 0:
    #                 print(f"{new_player} is out of health. Game over.")
    #                 session.commit()
    #                 return
    #             print("Please try again.")


    #         # update player and scoreboard objects with new score
    #         player1.score += score
    #         score1.score += score
    #         score1.games_completed += sum([getattr(room1, attr) for attr in room_attrs])
    #         session.commit()
    #         print("Your final score is", score)

    # # query the scoreboards and join them with the players
    # scoreboards = session.query(Scoreboard).join(Player).all()
    # for scoreboard in scoreboards:
    #     print(scoreboard.player.username, scoreboard.score, scoreboard.username)
