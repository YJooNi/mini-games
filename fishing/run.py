import fish
import player

# player created with 0 balance and empty list

player1 = player.Player()

# creation of different types of fish with rarity and value
cod = fish.Fish("Cod", 10, fish.rarity("common", "Cod"))
mackerel = fish.Fish("Mackerel", 10, fish.rarity("common", "Mackerel"))
flounder = fish.Fish("Flounder", 10, fish.rarity("common", "Flounder"))
salmon = fish.Fish("Salmon", 10, fish.rarity("common", "Salmon"))
seaBass = fish.Fish("Sea Bass", 10, fish.rarity("common", "Sea Bass"))
halibut = fish.Fish("Halibut", 10, fish.rarity("common", "Halibut"))
redMullet = fish.Fish("Red Mullet", 10, fish.rarity("common", "Red Mullet"))
pigfish = fish.Fish("Pigfish", 10, fish.rarity("common", "Pigfish"))
grouper = fish.Fish("Grouper", 10, fish.rarity("common", "Grouper"))
goldfish = fish.Fish("Goldfish", 100, fish.rarity("uncommon", "Goldfish"))
tuna = fish.Fish("Tuna", 500, fish.rarity("rare", "Tuna"))
fishWoman = fish.Fish("Fish Woman", 5000, fish.rarity("unique", "Fish Woman"))
mermaid = fish.Fish("Mermaid", 15000, fish.rarity("mythic", "Mermaid"))

# adding fish to a dictionary
fish.addFish(cod)
fish.addFish(mackerel)
fish.addFish(flounder)
fish.addFish(salmon)
fish.addFish(seaBass)
fish.addFish(halibut)
fish.addFish(redMullet)
fish.addFish(pigfish)
fish.addFish(grouper)
fish.addFish(goldfish)
fish.addFish(tuna)
fish.addFish(fishWoman)
fish.addFish(mermaid)

run = True

# catches fish
def catch_fish():
    result = fish.fishList.get(fish.lootTable())
    print("You caught a", result.name + "!", "It's value is", result.value, "gold.")
    player.addInventory(result.name, player1)
    print("The", result.name, "went into your inventory.")
    print("")


# this function shows inventory of a player
def show_inv():
        
        counts = {}

        for x in player1.inventory:

            if x not in counts:
                counts[x] = 0

            counts[x] +=1

        for key, value in counts.items():

            print(f"{key} x{value} (", (fish.fishList.get(key).value * value), "gold )")

        print("")    

# this allows a player to sell a fish
def sell_fish():

    print("Sell your fish:")
    show_inv()

    sell_selection = input("Which fish to sell?")
    if sell_selection in player1.inventory:

        counts = {}

        for x in player1.inventory:

            if x not in counts:
                counts[x] = 0
            counts[x] +=1

        if counts.get(sell_selection) > 1:

            print("Selling", sell_selection, "( Max:", counts.get(sell_selection), ")")
            sell_count = input("How Many would you like to sell?")

            if int(sell_count) <= counts.get(sell_selection) and int(sell_count) > 1:

                for x in range(int(sell_count)):

                    player1.inventory.remove(sell_selection)

                player1.balance += (fish.fishList.get(sell_selection).value * int(sell_count))
                print("You sold", "x" + sell_count, sell_selection, "for", (fish.fishList.get(sell_selection).value * int(sell_count)), "gold")

            else:

                print("You do not have " + sell_count + " amount")

        else:

            player1.inventory.remove(sell_selection)
            player1.balance += fish.fishList.get(sell_selection).value
            print("You sold a", sell_selection, "for", fish.fishList.get(sell_selection).value, "gold")

        print("")
    else:

        print(sell_selection, "is not a selection")
        print("")


# main game
while run:

    selection = input("Would you like to fish??(y/n)")
    match selection:

        case "y":

            catch_fish()

        case "n":

            run = False

        case "inv":

            print("Your Inventory:")
            show_inv()

        case "bal":

            print("Your balance:")
            print(player1.balance, "gold")
            print("")

        case "sell":

            sell_fish()

        case _:

            print(selection, "is not a selection.")
            print("")
