# Phase 3 Final Project - CLI-scape!

## Description

CLI-scape is a command line based escape room concept.  The app was written in Python with SQLAlchemy for database table management.  The game itself is modled off of real-life escape rooms.  You are given a series of puzzles or "rooms" to complete within a 12 minute time-limit.  You must answer a question correctly to move on to the next room.  After six rooms, you have escaped and completed the game.  You are given 3 hints to use and a total of 10 missed-guesses forcing you to really have to strategize and think about the answer.

## File tree

Most the app lives in the /lib folder.  The game script itself exists in game-cli.py and uses several other files to support.  Inside the /db folder, all classes for the table models are written in models.py.  In seed.py, SQLAlchemy is used to pre-load all the puzzle "rooms" into the database.  A debug.py file is included with ipdb for realtime debugging and a helpers.py with supporting functions for the 12 minutes timer is also included.  Alembic was used to initiate the escape_app database containing four separate tables for storing game data.

## Escape_app.db

The tables included are players, rooms, scoreboards, and escapes.  Players keeps a database of anyone who plays the game via id and username.  rooms is a seeded database containing the puzzles used in the game.  scoreboards is a shared table containing instances of a player and one of the rooms.  Each instance contains the number of times a player has played that room and a running total of the score for that room.  The escapes database contains instances for a complete 'run' of the game by a player.  Via player id, it contain data of how many rooms the player completed on their run, their score and how much time it took for them to complete their run.  All this data is intended to be used to create a leader board that considers a number of different factors when ranking inlcuding high scores and the time it took to complete rooms.

## Game execution

The game itself is cleverly executed using a while loop.  Once the timer is started, the game itself goes into a loop that only breaks under a few circumstances: if the player runs out of time, if the player runs out of guesses, or if the the player wins the game.  The condition of the loop cannot be broken while there are still rooms to complete, therefore when a player completes a room, if there are still rooms left, the next room will load instead.  3 hints are given to the player to use during the game pulled from the instances of the rooms themselves.  Each room only contains one hint.  Once a player is out of hints, the hints are no longer accessible.  Typing 'timeleft' into the prompt will also allow the player to check their remaining time.  When the timer gets below 1 min, the text will turn red.

## Running the game

Be sure to run 'pipenv install' and 'pipenv shell'.  Then, change into the /lib folder and run 'python game-cli.py' to start the game.  You can press 'control + C' to exit the game at anytime.  Enjoy!

