from db.models import Player

# will check to see if name is in list, if not will assign name a new player instance
# def get_current_player(name, list):
#     if name in list:
#         x = session.query(Player).filter(Player.username == name).first()
#         return x
#     else:
#         return Player(username=name)