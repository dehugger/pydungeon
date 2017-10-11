class Room(object):

    def __init__(self):
        #descriptors
        self.id = id
        self.name = name
        self.coord = coord

        #exits
        self.exit_west
        self.exit_north
        self.exit_east
        self.exit_south
        self.exit_up
        self.exit_down
        self.exit_other
        self.exit_west_status
        self.exit_north_status
        self.exit_east_status
        self.exit_south_status
        self.exit_up_status
        self.exit_down_status
        self.exit_other_status

        #contains
        self.characters = []
        self.items = []

