
class item:
    def __init__(self, name, description, type, stats, value):
        self.name = name
        self.description = description
        self.type = type
        self.stats = stats
        self.value = value

def item_stats(health, mana, str, dex, int):
    stats = {
        "health": health,
        "mana": mana,
        "str": str,
        "dex": dex,
        "int": int
    }
    return stats

wooden_sword = item("Wooden Sword", "A sword made out of wood", "primary_weapon", item_stats(0, 0, 2, 1, 0), 5)
