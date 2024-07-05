import menu
import game

run = True

while run:
    print(menu.display_main_menu)
    menu.create_menu(menu.list_main_menu)
    selection = input("Select an option:")
    match selection:
        case "1" :
            game.game_start(run)
            break
        case "2":
            print("Thank You For Playing!")
            run = False
            break 
        case _:
            print(selection, "is not an option!")