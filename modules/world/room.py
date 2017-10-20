from modules.functions.io import io
from modules.objects.exit import Exit

class Room(object):

    def __init__(self, id, name, description='A room', coord='1,1'):
        #descriptors
        self.id = id
        self.name = name
        self.description = description
        self.coord = coord

        #exits

        self.exits = []
        #this line is only in for testing. should be removed when actually using engine

        self.exits.append(Room.create_exit(self))

        #contains
        self.characters = []
        self.items = []

    def create_exit(self, name='Door', connects_to_room_id=1, location='north', description='A plain door', open_action='You open the door and step through', status='open', key=None):
        exit_var = Exit(name, connects_to_room_id, location, description, open_action, status, key)
        return exit_var

    def add_item(self, item):
        self.items.append(item)
