import character
import items

player = character.Character("Myname")


run = True

while run:
    print("Your Stats:")
    print(player.status)

    player.inventory.append(items.wooden_sword.name)
    print("You have recieved a Wooden Sword!")
    print(items.wooden_sword.__dict__)
    print("Your inventory:")
    print(player.inventory)
    selection = input("Would you like to equip this item?")

    match selection:
        case "yes":
            player.equipment["primary_weapon"] = items.wooden_sword
            print("You have equipped a Wooden Sword!")
        case _:
            "You have not equipped anything"

    if "primary_weapon" in player.equipment is not None:
        for x in player.status:
           player.status[x] = player.status[x] + player.equipment.get("primary_weapon").stats[x]
    
    print("Your equipment:")
    print(player.equipment)

    print("Your Stats:")
    print(player.status)
       
    run = False