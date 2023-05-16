from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Player, Scoreboard, Room


puzzle1 = Puzzle(

    points = 1000,
   
    body = 'M -> N  //  G -> T  //  K -> P  //  C -> ?',
    answer = 'X',
    hint = 'Go back to your ABCs'
)

puzzle2 = Puzzle(
    
    points = 1000,
 
    body = 'I am light as a feather, and can keep it aloft.  Most of the time I am silnet and soft.  I am with you always in whispers and song.  The strongest of men can\'t hold me for long.',
    answer = 'breath',
    hint = 'I am invisible but can be seen in the cold'
)