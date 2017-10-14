import _pickle
from modules.functions.io import io
from modules.objects.player import Player
from modules.world.room import Room
from modules.world.game import Game

def save_object(obj):
    save_name = 'saves/' + obj.name + '.p'
    _pickle.dump(obj, open(save_name, 'wb'), protocol=0)

def load_object(name):
    save_name = 'saves/' + name + '.p'
    name = _pickle.load( open(save_name, 'rb'))
    return name

def save_obj_list(obj_names):
    save_name = 'saves/objlist.p'
    _pickle.dump(obj_names, open(save_name, 'wb'))

def load_obj_names():
    save_name = 'saves/objlist.p'
    obj_names = _pickle.load(open(save_name, 'rb'))
    return obj_names

def save_game(objs, save_name='default'):
    class objNames():
        obj_names = []

    Objects = objNames()

    for obj in objs:
        save_object(obj)
        Objects.obj_names += obj.name

    save_obj_list(Objects)

    return 'Gamestate Saved'

def load_game():
    Objects = load_obj_names()
    objs = []
    for obj in Objects.obj_names:
        pass


def create_player():
    name = io.read('What is your players name?')
    new_player = Player(name)
    return new_player

def create_room():
    id = io.read('What is the rooms id?')
    name = io.read('What is the rooms name?')
    new_room = Room(id, name)
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