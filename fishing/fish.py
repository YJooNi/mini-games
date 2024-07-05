import random

fishList = {}

# creation of a fish object
class Fish:
    def __init__(self, name, value, rarity):
        self.name = name
        self.value = value
        self.rarity = rarity

common = []
uncommon = []
rare = []
unique = []
mythic = []

def rarity(type, name):
    match type:
        case "common":
            common.append(name)
        case "uncommon":
            uncommon.append(name)
        case "rare":
            rare.append(name)
        case "unique":
            unique.append(name)
        case "mythic":
            mythic.append(name)
    return type

def addFish(fish):
    fishList.update({fish.name: fish})

def lootTable():
    number = random.random()*100

    if number <= 65.5:
        return random.choice(common)
    elif number <= 85.5:
        return random.choice(uncommon)
    elif number <= 94.5:
        return random.choice(rare)
    elif number <= 99.4:
        return random.choice(unique)
    elif number > 99.4:
        return random.choice(mythic)
