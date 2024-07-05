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
    max = 2500
    number = random.randint(1, max)
    if number <= 1375:
        return random.choice(common)
    elif number <= 1875:
        return random.choice(uncommon)
    elif number <= 2250:
        return random.choice(rare)
    elif number <= 2425:
        return random.choice(unique)
    elif number > 2425 and number <= 2500:
        return random.choice(mythic)
