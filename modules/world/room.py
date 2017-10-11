class Room(object):

    def __init__(self, id, name, coord):
        #descriptors
        self.id = id
        self.name = name
        self.coord = coord

        #exits
        self.exit_west = None
        self.exit_north = None
        self.exit_east = None
        self.exit_south = None
        self.exit_up = None
        self.exit_down = None
        self.exit_other = None
        self.exit_west_status = None
        self.exit_north_status = None
        self.exit_east_status = None
        self.exit_south_status = None
        self.exit_up_status = None
        self.exit_down_status = None
        self.exit_other_status = None

        #contains
        self.characters = []
        self.items = []

