class Player(object):

    def __init__(self, name, type, race='Human', movement=30, health_max=50, inv_weight_max=100, inventory=[],
                 head=None, chest=None, shoulders=None,arms=None, hands=None, belt=None, legs=None, feet=None,
                 ring=None, neck=None, back=None, hand_main=None, hand_off=None,
                 strength=10, constitution=10, intelligence=10, charisma=10, dexterity=10):
        #Base Statistics
        self.name = name
        self.type = type
        self.race = race
        self.movement = movement
        self.health_max = health_max
        self.health_current = self.health_max
        self.inv_weight_max = inv_weight_max
        self.inventory = inventory
        #Equipment
        self.head = head
        self.chest = chest
        self.shoulders = shoulders
        self.arms = arms
        self.hands = hands
        self.belt = belt
        self.legs = legs
        self.feet = feet
        self.ring = ring
        self.neck = neck
        self.back = back
        self.hand_main = hand_main
        self.hand_off = hand_off
        #stats
        self.strength = strength
        self.constitution = constitution
        self.intelligence = intelligence
        self.charisma = charisma
        self.dexterity = dexterity

    def takeDamage(self, damage_taken):
        self.health_current = self.health_current - damage_taken
        return self.health_current

    def heal(self, healing_ammount):
        if self.health_max < self.health_current + healing_ammount:
            self.health_current = self.health_max
        else:
            self.health_current += healing_ammount
        return self.health_current

    def fullHeal(self):
        self.health_current = self.health_max
        return self.health_current

    def gainItem(self, item):
        self.inventory.append(item)
        return item.name + ' added to ' + self.name + '\'s inventory'

    def loseItem(self, item):
        if item in self.inventory:
            self.items.remove(item)
            return item.name + ' removed from ' + self.name + '\'s inventory'
        else:
            return item.name + ' could not be removed from ' + self.name + '\'s inventory because they did not have that item'