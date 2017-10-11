from modules.functions.io import io

class PlayerActions():

    def input_parse(player, room):
        raw = io.read('what would you like to do?')
        raw_split = raw.split()
        if raw_split[0] == 'inspect':
            if raw_split[1] == 'room':
                PlayerActions.inspect_room(player, room)
            else:
                io.log('Sorry, I dont know what you want to inspect.')
        elif raw_split[0] == 'exit':
            exit()
        else:
            io.log('Sorry, I did not understand what you want to do.')

    def inspect_room(player, room):

        io.log(player.name + ' looks about the room, observing all details. They see:')
        io.log(room.exit_west)
        for item in room.items:
            io.log(item.description)

        for character in room.characters:
            io.log(character.description)