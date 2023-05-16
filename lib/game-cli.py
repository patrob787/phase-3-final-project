from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Player, Scoreboard, Room,  Base
# from sqlalchemy.sql.expression import func

engine = create_engine("sqlite:///escape_app.db", echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':

    # session.query(Player).delete()

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
        
        current_player = Player(username=new_player)
        
        session.add(current_player)
        session.commit()
        
        current_player.score = 0
        current_player.attempts = 5
        current_player.hints = 3

        print(f'Score: {current_player.score}, Attempts left: {current_player.attempts}, Hints left:{current_player.hints}')
        

        print(f"{new_player} you have been trapped inside of the CLI.  Your only chance at escaping is to complete a gauntlet of challenges.  There are ?? challenges in total to complete.  You'll have a total of 10 missed-attempts and 3 hints to use at anytime.  If you run out of attempts, the game is lost.  For each room you complete you will recieve points.  For escaping the CLI you will recieve a bonus score!")
        input("Press enter when you are ready to CLI-scape!  Good luck!")

        rooms = session.query(Room).all()
        i = 0
       
        print(f"ROOM {i + 1}")

        
        print(f"""
            {rooms[i].body}
        """)
            
        while (i < len(rooms)):
            
            input1 = input("Input your answer or ask for a hint with 'hint': ")
            
            if input1.lower() == rooms[i].answer.lower():
                print('Correct!')
                
                current_player.score += rooms[1].points

                new_score_record = Scoreboard(player_id=current_player.id, room_id=rooms[i].id, score=rooms[i].points)
                session.add(new_score_record)
                session.commit()
                
                i += 1

                if (i == len(rooms)):
                    print("Good Job!  You CLI-scaped!!")
                    break
                else:
                    print(f"Your current score is {current_player.score}!")
                    print(f"ROOM {i + 1}")
                    print(f"""
                    {rooms[i].body}
                        """) 
            elif input1 == 'hint':
                if (current_player.hints > 0):
                    print(f"{rooms[i].hint}")
                    current_player.hints -= 1
                    print(f"You have {current_player.hints} hints left.")
                else:
                    print('You have run out of hints.')
            else:
                print("incorrect!")
                current_player.attempts -= 1
                if (current_player.attempts > 0):
                    print(f"You have {current_player.attempts} guesses left.")
                else:
                    print('You have died.  GAMEOVER!')
                    break

        
    else:
        print("Ah well... good luck finding your way home!")
