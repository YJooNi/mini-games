
class Player:
    def __init__(self, balance):
        self.inventory = []
        self.balance = balance

def addInventory(fish_name, player):
    player.inventory.append(fish_name)