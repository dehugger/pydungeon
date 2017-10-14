class Game(object):

    def __init__(self, name, player, active_room):
        self.name = name
        self.player = player
        self.active_room = active_room
        self.all_rooms = []
        self.all_rooms.append(active_room)

    def AddRoom(self, room):
        self.all_rooms.append(room)