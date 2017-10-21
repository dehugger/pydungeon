class Player(object):

    def __init__(self, name, race='Human', movement=30, health_max=50, inv_weight_max=100, inventory=[],
                 head=None, chest=None, shoulders=None,arms=None, hands=None, belt=None, legs=None, feet=None,
                 ring=None, neck=None, back=None, hand_main=None, hand_off=None,
                 strength=10, constitution=10, intelligence=10, charisma=10, dexterity=10):
        #Base Statistics
        self.name = name
        self.type = 'player'
        self.race = race
        self.movement = movement
        self.base_health_max = health_max
        self.health_max = self.base_health_max
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
        self.equipmentUpdate()
        #stats
        self.strength = strength
        self.constitution = constitution
        self.intelligence = intelligence
        self.charisma = charisma
        self.dexterity = dexterity

        self.calculateMaxHealth()

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

    def equipmentUpdate(self):
        self.equipment = [self.head, self.shoulders, self.chest, self.arms, self.hands, self.back, self.belt, self.legs, self.feet, self.hand_main, self.hand_off, self.ring, self.neck]

    def calculateMaxHealth(self):
        health_max_boost = 0
        for item in self.equipment:
            if item != None:
                health_max_boost += item.health_effect
        self.health_max = self.base_health_max + health_max_boost

    def getPlayerStats(self):
        player_stats = '''
        \n
        %(name)s Stats:\n
        <-------------------------------------------->\n
        HP Max         - %(maxhp)s \n
        HP Current     - %(currenthp)s \n
        Weight Max     - %(maxweight)s \n
        Weight Carried - Not Implemented \n
        Strength       - %(strength)s \n
        Constitution   - %(constitution)s \n
        Intelligence   - %(intelligence)s \n
        Dexterity      - %(dexterity)s \n
        Charisma       - %(charisma)s \n
        <-------------------------------------------->
        ''' % {
            'name': self.name,
            'maxhp': self.health_max,
            'currenthp': self.health_current,
            'maxweight': self.inv_weight_max,
            'strength': self.strength,
            'constitution': self.constitution,
            'intelligence': self.intelligence,
            'dexterity': self.dexterity,
            'charisma': self.charisma
        }

        return player_stats