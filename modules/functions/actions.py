from modules.functions.io import io
from modules.functions.gamestate import save_object
from modules.functions.gamestate import create_room, create_item

class PlayerActions():

    def obj_search(game, search_level, name):
        if search_level == 'player':
            for obj in game.player.inventory:
                if obj.name == name:
                    return obj
                else:
                    pass
            io.log('The player doesnt have that object.')
            return None

        elif search_level == 'room':
            for obj in game.active_room.items:
                if obj.name == name:
                    return obj
                else:
                    pass
            for obj in game.active_room.exits:
                if obj.name == name:
                    return obj
                else:
                    pass
            io.log('That object isnt in the room!')
            return None

        elif search_level == 'the':
            for obj in game.active_room.items:
                if obj.name == name:
                    return obj
                else:
                    pass
            for obj in game.active_room.exits:
                if obj.name == name:
                    return obj
                else:
                    pass
            io.log('That object isnt in the room!')
            return None

        elif search_level == None:
            for obj in game.active_room.items:
                if obj.name == name:
                    return obj
                else:
                    pass
            for obj in game.active_room.exits:
                if obj.name == name:
                    return obj
                else:
                    pass
            for obj in game.player.inventory:
                if obj.name == name:
                    return obj
                else:
                    pass
            io.log('That object could not be found.')
            return None

        elif search_level == 'to':
            for obj in game.active_room.characters:
                if obj.name == name:
                    return obj
                else:
                    pass
            for obj in game.all_rooms:
                if obj.name == name:
                    return obj
                else:
                    pass
            io.log('That object could not be found.')
            return None

        else:
            for character in game.active_room.characters:
                if character.name == search_level:
                    for item in character.inventory:
                        if item.name == name:
                            return item
                        else:
                            pass
                else:
                    pass
            for obj in game.active_room.items:
                if obj.name == name:
                    return obj
                else:
                    pass
            for obj in game.active_room.exits:
                if obj.name == name:
                    return obj
                else:
                    pass
            for obj in game.player.inventory:
                if obj.name == name:
                    return obj
                else:
                    pass
            io.log('The object you were looking for was not found.')
            return None

    def top_actions(key, obj, game):
        io.log('executing action ' + key)
        actions = {
            'inspect': PlayerActions.inspect_object,
            'take': PlayerActions.take_object,
            'find': PlayerActions.find,
            'save': PlayerActions.save,
            'exit': PlayerActions.action_exit,
            'equip': PlayerActions.equip,
            'createroom': PlayerActions.add_room,
            'moveroom':PlayerActions.move_room,
            'createitem': PlayerActions.add_item
        }

        #try:
        actions[key](game, obj)
        #except:
            #io.log('action execution error')

    def mid_level_special_cases(key, game):
        return {
            'room': game.active_room
        }.get(key, None)

    def input_parse(game):

        special_args = ['room']

        user_input = io.read('what would you like to do?')
        if user_input == '':
            return
        user_input_split = user_input.split()
        action = user_input_split[0]
        arg_count = len(user_input_split) - 1

        if arg_count == 2:
            arg_one = user_input_split[1]
            arg_two = user_input_split[2]
            if arg_one in special_args:
                PlayerActions.top_actions(action, PlayerActions.mid_level_special_cases(arg_one, game), game)
            else:
                obj = PlayerActions.obj_search(game, arg_one, arg_two)
                PlayerActions.top_actions(action, obj, game)

        elif arg_count == 1:
            arg = user_input_split[1]
            if arg in special_args:
                PlayerActions.top_actions(action, PlayerActions.mid_level_special_cases(arg, game), game)
            else:
                obj = PlayerActions.obj_search(game, None, arg)
                PlayerActions.top_actions(action, obj, game)

        elif arg_count == 0:
            PlayerActions.top_actions(action, None, game)

        elif arg_count > 2:
            io.log('To many action arguments!')


    def inspect_room(game, room):

        io.log(game.player.name + ' looks about the room, observing all details. They see:')
        for exit in room.exits:
            io.log(exit.location)
            io.log(exit.description)

        for item in room.items:
            io.log(item.description)

        for character in room.characters:
            io.log(character.description)

    def inspect_object(game, object):
        if object == None:
            pass
        else:
            io.log(game.player.name + ' takes a close look at ' + object.name)
            io.log(object.name + ', ' + object.description)

    def take_object(game, object):
        if object == None:
            pass
        else:
            game.active_room.items.remove(object)
            game.player.inventory.append(object)
            object.location = game.player.name
            object.location_description = 'The players inventory.'
            io.log(game.player.name + ' takes ' + object.name + ' from ' + game.active_room.name + ' and puts it in their inventory.')

    def find(game, object):
        if object == None:
            pass
        else:
            io.log(object.location + ', ' + object.location_description)

    def move_room(game, new_room):
        if new_room == None:
            pass
        else:
            old_room = game.active_room
            game.active_room = new_room
            message = game.player.name + ' leaves ' + old_room.name + ' and enters ' + new_room.name
            io.log(message)

    def equip(game, obj):
        if obj == None:
            pass
        else:
            if obj.location == game.player.name:
                if obj.type == 'Weapon' or obj.type == 'Armor':
                    game.player.inventory.remove(obj)
                    #repeat for every single item slot
                    if obj.item_slot == 'hand_main':
                        if game.player.hand_main == None:
                            game.player.hand_main = obj
                        else:
                            game.player.inventory.append(game.player.hand_main)
                            game.player.hand_main = obj
                    else:
                        io.log('Item cannot be equipped or item slot is not yet implemented')
            else:
                io.log('That item is not in the players inventory. You must take the item before you can equip it!')


#actions below are utilities for interacting with the gamestate, not true player actions

    def save(game, obj):
        save_object(game)
        io.log('Game Saved')

    def action_exit(game, obj):
        exit()

    def add_room(game, obj):
        room = create_room()
        game.AddRoom(room)
        io.log(room.name + ' added to game')

    def add_item(game, obj):
        item = create_item(game)
        game.active_room.items.append(item)
        io.log(item.name + ' added to game')