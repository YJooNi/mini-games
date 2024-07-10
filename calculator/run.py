import calculation
import menu

list_main_menu = [{"option": "START BASIC MATHAMATICS", "func": calculation.calculation_menu}, {"option": "END PROGRAM", "func": exit}]


run = True 
while run:
    while True:
        print(menu.display_main_menu)
        menu.create_menu(list_main_menu)
