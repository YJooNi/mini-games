
character_base_status = {
    "health" : 10,
    "mana" : 5,
    "str" : 5,
    "dex" : 5,
    "int" : 5
}

character_equipment = {
    "primary_weapon": None,
    "helmet": None,
    "chestpiece": None,
    "legs": None,
    "boots": None
}

class Character:
    def __init__(self, name):
        self.name = name
        self.status = character_base_status
        self.inventory = []
        self.equipment = character_equipment
