class Item(object):

    def __init__(self,id, location, location_description, name, type, owner, weight=1, physics=True, description='An Item'):
        #descriptors
        self.id = id
        self.location = location
        self.location_description = location_description
        self.name = name
        self.type = type
        self.owner = owner
        self.weight = weight
        self.physics = physics
        self.description = description

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getOwner(self):
        return self.owner

    def getWeight(self):
        return self.weight

    def getPhysics(self):
        return self.physics

    def getDescription(self):
        return self.description

    def __str__(self):
        return "{} is a {}. It weighs {}. {}".format(self.name, self.type, self.weight, self.description)


class Weapon(Item):

    def __init__(self, name, owner, weight=1, range='melee', damage=1, damage_type='raw', item_slot=hand_main, description='A Blade'):
        Item.__init__(self, name, 'Weapon', owner, weight, True, description)
        self.range = range
        self.damage = damage
        self.damage_type = damage_type
        self.item_slot = item_slot

    def getDamage(self):
        return self.damage

    def getDamageType(self):
        return self.damage_type

    def getRange(self):
        return self.range

    def __str__(self):
        return "{}, range {}, damage {}, damage type {}".format(self.name, self.range, self.damage, self.damage_type)