import calculation
import menu

run = True  
while run:
    while True:
        print(menu.display_main_menu)
        menu.create_menu(menu.list_main_menu)
        selection = input("Select an option:")
        match selection:
            case "1" :
                calculation.calculation_menu()
                break
            case "2":
                print("Thank You!")
                run = False
                break 
            case _:
                print(selection, "is not an option!")
                break