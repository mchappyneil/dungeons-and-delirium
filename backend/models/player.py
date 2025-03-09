class Player:
    def __init__(self):
        self.stats = {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10
        }
        self.armor_class = 10
        self.hit_points = 10
        self.level = 1
        self.successful_checks = 0
        self.equipment = []
        self.class_name = None
        self.class_desc = None
        
    def level_up(self):
        self.level += 1
        self.hit_points += 5
        self.successful_checks = 0
        for stat in self.stats:
            self.stats[stat] += 1
    
    def to_dict(self):
        return {
            "class_name": self.class_name,
            "class_description": self.class_description,
            "stats": self.stats,
            "armor_class": self.armor_class,
            "hit_points": self.hit_points,
            "level": self.level,
            "successful_checks": self.successful_checks,
            "equipment": self.equipment,
        }

class Fighter(Player):
    def __init__(self):
        super().__init__()
        self.armor_class = 12
        self.stats = {
            "Strength": 17,
            "Dexterity": 13,
            "Constitution": 15,
            "Intelligence": 10,
            "Wisdom": 12,
            "Charisma": 8
        }
        self.hit_points = 15 # Base HP for Fighter class
        self.class_name = "Fighter"
        self.class_description = (
            "Fighters rule many battlefields. Questing knights, royal champions, elite soldiers, and hardened mercenaries—as Fighters, "
            "they all share an unparalleled prowess with weapons and armor."
        )

class Bard(Player):
    def __init__(self):
        super().__init__()
        self.armor_class = 13
        self.stats = {
            "Strength": 8,
            "Dexterity": 15,
            "Constitution": 13,
            "Intelligence": 12,
            "Wisdom": 10,
            "Charisma": 17
        }
        self.hit_points = 10 # Base HP for Bard class
        self.class_name = "Bard"
        self.class_description = (
            "Invoking magic through music, dance, and verse, Bards are expert at inspiring others, soothing hurts, disheartening foes, "
            "and creating illusions. Their life is spent traveling, gathering lore, telling stories, and living on the gratitude of audiences."
        )


class Ranger(Player):
    def __init__(self):
        super().__init__()
        self.armor_class = 15
        self.stats = {
            "Strength": 12,
            "Dexterity": 17,
            "Constitution": 13,
            "Intelligence": 8,
            "Wisdom": 15,
            "Charisma": 10
        }
        self.hit_points = 11 # Base HP for Ranger class
        self.class_name = "Ranger"
        self.class_description = (
            "Rangers keep their unending watch in the wilderness. They learn to track their quarry as a predator does, "
            "moving stealthily through the wilds and hiding themselves in brush and rubble."
        )


class Wizard(Player):
    def __init__(self):
        super().__init__()
        self.armor_class = 12
        self.stats = {
            "Strength": 8,
            "Dexterity": 13,
            "Constitution": 15,
            "Intelligence": 17,
            "Wisdom": 10,
            "Charisma": 12
        }
        self.hit_points = 11 # Base HP for Wizard class
        self.class_name = "Wizard"
        self.class_description = (
            "Wizards are defined by their exhaustive study of magics inner workings. They cast spells of explosive fire, arcing lightning, "
            "subtle deception, and spectacular transformations. Their magic conjures monsters, glimpses the future, or forms protective barriers."
        )


class Rogue(Player):
    def __init__(self):
        super().__init__()
        self.armor_class = 14
        self.stats = {
            "Strength": 8,
            "Dexterity": 17,
            "Constitution": 14,
            "Intelligence": 13,
            "Wisdom": 13,
            "Charisma": 10
        }
        self.hit_points = 10 # Base HP for Rogue class
        self.class_name = "Rogue"
        self.class_description = (
            "Rogues rely on cunning, stealth, and exploiting their foes vulnerabilities. They excel in subtle strikes over brute force, "
            "preferring one precise blow to a barrage of hits."
        )


class Cleric(Player):
    def __init__(self):
        super().__init__()
        self.armor_class = 10
        self.stats = {
            "Strength": 15,
            "Dexterity": 10,
            "Constitution": 13,
            "Intelligence": 8,
            "Wisdom": 17,
            "Charisma": 12
        }
        self.hit_points = 10 # Base HP for Cleric class
        self.class_name = "Cleric"
        self.class_description = (
            "Clerics draw power from the divine. Blessed by a deity, they harness miracles and channel divine magic to bolster allies and vanquish foes."
        )

# Factory method for creating a player by class name
def create_player(chosen_class: str):
    mapping = {
        "Fighter": Fighter,
        "Bard": Bard,
        "Ranger": Ranger,
        "Wizard": Wizard,
        "Rogue": Rogue,
        "Cleric": Cleric
    }
    if chosen_class not in mapping:
        raise ValueError("Invalid class selection.")
    return mapping[chosen_class]()