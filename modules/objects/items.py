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

    def __init__(self, id, location, location_description, name, owner, weight=1, item_slot='hand_main', description='A Blade', range='melee', damage=1, damage_type='raw'):
        Item.__init__(self, id, location, location_description, name, 'Weapon', owner, weight, True, description)
        self.range = range
        self.damage = damage
        self.damage_type = damage_type
        self.item_slot = item_slot
        self.noise_factor = 0
        self.strength_effect = 0
        self.constitution_effect = 0
        self.intelligence_effect = 0
        self.charisma_effect = 0
        self.dexterity_effect = 0
        self.health_effect = 0

    def getDamage(self):
        return self.damage

    def getDamageType(self):
        return self.damage_type

    def getRange(self):
        return self.range

    def __str__(self):
        return "{}, range {}, damage {}, damage type {}".format(self.name, self.range, self.damage, self.damage_type)


class Armor(Item):

    def __init__(self, id, location, location_description, name, owner, weight=1, item_slot='chest', description='A leather jerkin', physical_protection=1, fire_protection=0, lightning_protection=0, psychic_protection=0, noise_factor=0, strength_effect=0, constitution_effect=0, intelligence_effect=0, charisma_effect=0, dexterity_effect=0, health_effect=10):
        Item.__init__(self, id, location, location_description, name, 'Armor', owner, weight, True, description)
        self.item_slot = item_slot
        self.physical_protection = physical_protection
        self.fire_protection = fire_protection
        self.lightning_protection = lightning_protection
        self.psychic_protection = psychic_protection
        self.noise_factor = noise_factor
        self.strength_effect = strength_effect
        self.constitution_effect = constitution_effect
        self.intelligence_effect = intelligence_effect
        self.charisma_effect = charisma_effect
        self.dexterity_effect = dexterity_effect
        self.health_effect = health_effect