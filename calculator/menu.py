list_main_menu = ["START BASIC MATHAMATICS", "END PROGRAM"]
list_calculation_menu = ["ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "GO BACK"]

display_main_menu = "=== MAIN MENU ==="

def create_menu(arr):
    i = 1
    for x in arr:
        print(i, ". ", x)
        i+=1

