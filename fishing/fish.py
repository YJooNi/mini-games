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
    



# creation of different types of fish with rarity and value
cod = Fish("Cod", 10, rarity("common", "Cod"))
mackerel = Fish("Mackerel", 10, rarity("common", "Mackerel"))
flounder = Fish("Flounder", 10, rarity("common", "Flounder"))
salmon = Fish("Salmon", 10, rarity("common", "Salmon"))
seaBass = Fish("Sea Bass", 10, rarity("common", "Sea Bass"))
halibut = Fish("Halibut", 10, rarity("common", "Halibut"))
redMullet = Fish("Red Mullet", 10, rarity("common", "Red Mullet"))
pigfish = Fish("Pigfish", 10, rarity("common", "Pigfish"))
grouper = Fish("Grouper", 10, rarity("common", "Grouper"))
goldfish = Fish("Goldfish", 100, rarity("uncommon", "Goldfish"))
tuna = Fish("Tuna", 250, rarity("rare", "Tuna"))
fishWoman = Fish("Fish Woman", 1000, rarity("unique", "Fish Woman"))
fishMan = Fish("Fish Man", 1000, rarity("unique", "Fish Man"))
mermaid = Fish("Mermaid", 25000, rarity("mythic", "Mermaid"))

# adding fish to a dictionary
addFish(cod)
addFish(mackerel)
addFish(flounder)
addFish(salmon)
addFish(seaBass)
addFish(halibut)
addFish(redMullet)
addFish(pigfish)
addFish(grouper)
addFish(goldfish)
addFish(tuna)
addFish(fishWoman)
addFish(fishMan)
addFish(mermaid)
