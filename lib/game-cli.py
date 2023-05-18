from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Player, Scoreboard, Room,  Base
from helpers import start_timer
import time

engine = create_engine("sqlite:///escape_app.db", echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':

    input("\033[92mHello...and welcome to...")

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
    new_player = ""

    while (len(new_player) == 0 or len(new_player) > 10):
        new_player = input("Enter your name: ") # get the player's name from input stores in variable

        if 0 < len(new_player) <= 10:
            break
        else:
            print("Username must be between 1 and 10 characters")

    print(f'Welcome {new_player}!  Are you ready to begin?')
    start_game = input('Y/n ?: ')
    
    if start_game.lower() == 'y' or start_game.lower() == 'yes':
        
        all_players = session.query(Player).all()
        player_names = [player.username for player in all_players]

        if new_player in player_names:
            current_player = session.query(Player).filter(Player.username == new_player).first()
        else:
            current_player = Player(username=new_player)
       
        
        session.add(current_player)
        session.commit()
        
        current_player.score = 0
        current_player.attempts = 10
        current_player.hints = 3

        
        print(f"""
        
        Oh no, {new_player}!  You have been trapped inside of the CLI!!  
        Your only chance at escaping is to complete a gauntlet of challenges.  
        There are 6 challenges in total you must finish in order to escape.  
        You'll have 10 missed-guesses and 3 hints to use at anytime.  A hint can only be used once per room.  
        If you run out of guesses, the game is lost and you will be trapped inside the CLI FOREVER!!  
        For each room you complete you will recieve points.  If you escape the CLI you will recieve a bonus score!
        Good Luck!
        
        """)
        input("Press ENTER when you are ready to CLI-SCAPE!")

        rooms = session.query(Room).all()
        i = 0
        hint_count = 1

        print(f"""
        ROOM {i + 1}
        Player: {current_player.username}
        Score: {current_player.score}
        Guesses Remaining: {current_player.attempts}
        Hints Remaining: {current_player.hints}
        """)

        input("Press ENTER to continue...")
                    
        print(f"""
                        
        {rooms[i].body}
        
        """)
        
        # set the duration of the timer (in seconds)
        timer_duration = 60
        
        # start the timer
        time_left = True
        end_time = start_timer(timer_duration)

         
        while (time_left) and (i < len(rooms)):

            time_remaining = int(end_time - time.time())
            if time_remaining < 0:
                time_left = False
                break
            
            if time_remaining <= 10:
                print("\033[31m")  # set the text color to red
            print(f"Time remaining: {time_remaining} seconds\n")
            
            input_answer = input("Type your answer or ask for a hint with 'hint': ")
        
            time_remaining = int(end_time - time.time())
            
            if time_remaining > 0 and input_answer.lower() == rooms[i].answer.lower():
                input(f"Correct!  You get {rooms[i].points} points!  Press ENTER to continue.")

                current_player.score += rooms[i].points

                room_records = session.query(Scoreboard).filter(Scoreboard.room_id == rooms[i].id).all()
                room_player_ids = [record.player_id for record in room_records] 

                if current_player.id in room_player_ids:
                    update_room_record = session.query(Scoreboard).filter(Scoreboard.player_id == current_player.id, Scoreboard.room_id == rooms[i].id).first()
                    update_room_record.count += 1
                    update_room_record.total_score *= update_room_record.count
                    session.commit()
                
                else:
                    new_room_record = Scoreboard(player_id=current_player.id, room_id=rooms[i].id, count=1, total_score=rooms[i].points)
                    session.add(new_room_record)
                    session.commit()
                
                i += 1

                if (i == 6):
                    current_player.score += 5000
                    print("""
  ______   ______   .__   __.   _______ .______          ___   .___________. __    __   __          ___   .___________. __    ______   .__   __.      _______. __  
 /      | /  __  \  |  \ |  |  /  _____||   _  \        /   \  |           ||  |  |  | |  |        /   \  |           ||  |  /  __  \  |  \ |  |     /       ||  | 
|  ,----'|  |  |  | |   \|  | |  |  __  |  |_)  |      /  ^  \ `---|  |----`|  |  |  | |  |       /  ^  \ `---|  |----`|  | |  |  |  | |   \|  |    |   (----`|  | 
|  |     |  |  |  | |  . `  | |  | |_ | |      /      /  /_\  \    |  |     |  |  |  | |  |      /  /_\  \    |  |     |  | |  |  |  | |  . `  |     \   \    |  | 
|  `----.|  `--'  | |  |\   | |  |__| | |  |\  \----./  _____  \   |  |     |  `--'  | |  `----./  _____  \   |  |     |  | |  `--'  | |  |\   | .----)   |   |__| 
 \______| \______/  |__| \__|  \______| | _| `._____/__/     \__\  |__|      \______/  |_______/__/     \__\  |__|     |__|  \______/  |__| \__| |_______/    (__) 
                                                                                            
                    """)
                    print(f"You CLI-scaped!!  Well Done!  Your final score is {current_player.score}!")
                    print("Thank you for playing!")
                    break
                
                else:
                    hint_count = 1

                    print(f"""
        ROOM {i + 1}
        Player: {current_player.username}
        Score: {current_player.score}
        Guesses Remaining: {current_player.attempts}
        Hints Remaining: {current_player.hints}
                    """)

                    input("Press ENTER to continue...")

                    print(f"""
            
        {rooms[i].body}
                    
                    """)

            elif input_answer == 'hint':
                if (time_remaining > 0) and (current_player.hints > 0) and (hint_count == 1):
                    print(f"{rooms[i].hint}")
                    current_player.hints -= 1
                    hint_count = 0
                elif (current_player.hints > 0 and hint_count == 0):
                    print("You have already used a hint for this room.")
                else:
                    print("You have run out of hints.")
            
            else:
                print("incorrect!")
                current_player.attempts -= 1
                if (current_player.attempts > 0) and (time_remaining > 0):
                    print(f"You have {current_player.attempts} guesses remaining.")
                else:
                    break


        print(f"Rats!  You almost made it.  Your final score is {current_player.score}.")
        print("""
.----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. |
| |    ______    | || |      __      | || | ____    ____ | || |  _________   | | | |     ____     | || | ____   ____  | || |  _________   | || |  _______     | |
| |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | | | |   .'    `.   | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | |
| | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | | | |  /  .--.  \  | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | |
| | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | | | |  | |    | |  | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | |
| | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | | | |  \  `--'  /  | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | |
| |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | | | |   `.____.'   | || |     \_/      | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' |
'----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------' 

        """)

    else:
        print("Ah well... come back soon!")
