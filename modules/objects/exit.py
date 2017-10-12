class Exit(object):

    def __init__(self, name, location='north', description='A plain door', open_action='You open the door and step through', status='open', key=None):
        self.name = name
        self.location = location
        self.description = description
        self.open_action = open_action
        self.key = key
        self.status = status