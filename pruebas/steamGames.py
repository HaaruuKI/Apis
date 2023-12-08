from __future__ import print_function
import json
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam(KEY)

# arguments: search
user = steam.apps.search_games("terr")

print(json.dumps(user, indent=4))
# for game in user["apps"]:
  
#     print(user["apps"]["name"])
#     print(game["price"])
#     print(user["apps"]["img"])