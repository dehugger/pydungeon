class Exit(object):

    def __init__(self, name, connects_to_room_id=1, location='north', description='A plain door', open_action='You open the door and step through', status='open', key=None):
        self.name = name
        self.connects_to_room_id = connects_to_room_id
        self.location = location
        self.description = description
        self.open_action = open_action
        self.key = key
        self.status = status