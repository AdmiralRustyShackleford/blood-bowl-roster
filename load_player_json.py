# a script for loading a JSON file into the database as model objects


import json
from bbd.models import Player

with open('players.json') as f:
    players_json = json.load(f)

for player in players_json:
    player = Player(first_name=player['first_name'],
                    last_name=player['last_name'],
                    number=player['number'],
                    MA=player['MA'],
                    ST=player['ST'],
                    AG=player['AG'],
                    AV=player['AV'],
                    team=player['team'],
                    position=player['position'],
                    spp=player['spp'],
                    )
    player.save()
