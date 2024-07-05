
class Player:
    def __init__(self):
        self.inventory = []
        self.balance = 0

def addInventory(fish_name, player):
    player.inventory.append(fish_name)