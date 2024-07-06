import fish
import player
import time
import random

# player created with 0 balance and empty list

player1 = player.Player()

run = True

# catches fish
def catch_fish():

    # adds a delay to fishing
    print("Throwing a fishing line", end=" ", flush=True)
    for x in range(random.randint(3,7)):
            print(".", end=" ", flush=True)
            time.sleep(0.7)
    print("")

    number = random.random()
    if number <= .75:
        result = fish.fishList.get(fish.lootTable())
        print("You caught a", result.name + "!", "It's value is", result.value, "gold.")
        player.addInventory(result.name, player1)
        print("The", result.name, "went into your inventory.")
        print("")
    else:
        print("Line came back empty...")
        print("")

# function for counting inventory
def countFish(counts):

    for x in player1.inventory:
        if x not in counts:
            counts[x] = 0
        counts[x] +=1

    return counts

# this function shows inventory of a player
def show_inv():
        
        counts = {}

        countFish(counts)

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

        countFish(counts)

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


# shop to buy items
def shop():
    print("Welcome to the fish shop")

# main game
while run:

    selection = input("Would you like to fish? ( y / n | inv / bal / sell / shop):")
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

        case "shop":

            shop()

        case _:

            print(selection, "is not a selection.")
            print("")
