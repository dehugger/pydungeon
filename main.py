from modules.functions.gamestate import *
from modules.functions.io import io
from modules.objects.player import Player
from modules.world.room import Room
from modules.world.game import Game
from modules.functions.actions import PlayerActions



game = load_or_new_game()
io.log(game.player.name)
io.log(game.active_room.name)
io.log(game.name)
while True:
    PlayerActions.input_parse(game)