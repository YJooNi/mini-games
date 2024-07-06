class Material:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Rod:
    def __init__(self, name, description, level, sell_cost):
        self.name = name
        self.description = description
        self.level = level
        self.sell_cost = sell_cost


# crafted Rods 
beginnerFishingRod = Rod("Beginner Fishing Rod","A fishing rod for beginners", 1, 100)
basicFishingRod = Rod("Basic Fishing Rod", "A fishing rod that is basic", 1, 1500)


# Materials for the shop
basicHandle = Material("Basic Handle", 100)
basicRod = Material("Basic Rod", 500)
basicGuides = Material("Basic Guides", 500)
basicFishingLine = Material("Basic Fishing Line", 300)
basicReel = Material("Basic Reel", 600)

