from modules.functions.gamestate import save_object, load_object
from modules.functions.io import io
from modules.objects.player import Player
from modules.world.room import Room
from modules.world.game import Game
from modules.functions.actions import PlayerActions


def create_player():
    name = io.read('What is your players name?')
    new_player = Player(name)
    return new_player

def create_room():
    id = io.read('What is the rooms id?')
    name = io.read('What is the rooms name?')
    coord = io.read('What is the rooms Coord?')
    new_room = Room(id, name, coord)
    return new_room

def create_game(player, room):
    name = io.read('What is the game name?')
    new_game = Game(name, player, room)
    save_object(new_game)
    return new_game

def load_or_new_game():
    choice = io.read('Would you like to load a game?')
    if choice in ['y', 'Y', 'yes', 'Yes']:
        game = load_object('new_game')
    else:
        player = create_player()
        room = create_room()
        game = create_game(player, room)

    return game




game = load_or_new_game()
io.log(game.player.name)
io.log(game.active_room.name)
io.log(game.name)
while True:
    PlayerActions.input_parse(game.player, game.active_room)