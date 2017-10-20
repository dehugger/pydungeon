import _pickle
from modules.functions.io import io
from modules.objects.player import Player
from modules.world.room import Room
from modules.world.game import Game
from modules.objects.items import Item, Weapon

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

def load_or_new_game():
    while True:
        choice = io.read('Would you like to load a game?')
        if choice in ['y', 'Y', 'yes', 'Yes', 'YES']:
            game_name = io.read('What is the name of your save file?')
            game = load_object(game_name)
            break
        elif choice in ['n', 'N', 'no', 'No', 'NO']:
            player = create_player()
            room = create_room()
            game = create_game(player, room)
            break
        else:
            pass
    return game

def create_game(player, room):
    name = io.read('What is the game name?')
    new_game = Game(name, player, room)
    save_object(new_game)
    return new_game

#functions below allow creating objects. they are for testing and dev purposes

def create_player():
    name = io.read('What is your players name?')
    new_player = Player(name)
    return new_player

def create_room():
    id = io.read('What is the rooms id?')
    name = io.read('What is the rooms name?')
    new_room = Room(id, name)
    return new_room

def create_item(game):
    type_prompt = '''
    What is the item type?\n
    1. Item
    2. Weapon
    3. Armor
    4. Consumable
    '''
    type = io.read(type_prompt)
    name = io.read('What is the item name?')
    id = io.read('What is the item ID?')
    location = game.active_room.name
    location_description = io.read('Where is the item in the room?')
    owner = game.player.name

    if type in ['1', 'item', 'Item', 'ITEM']:
        new_item = Item(id, location, location_description, name, type, owner)

    elif type in ['2', 'weapon', 'Weapon', 'WEAPON']:
        new_item = Weapon(id, location, location_description, name, owner)

    elif type in ['3', 'armor', 'Armor', 'ARMOR']:
        new_item = None
    elif type in ['4', 'consumable', 'Consumable', 'CONSUMABLE']:
        new_item = None

    return new_item

