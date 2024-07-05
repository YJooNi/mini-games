list_main_menu = ["PLAY", "END PROGRAM"]
list_game_menu = ["PLAY AGAIN", "END PROGRAM"]

display_main_menu = "===== MAIN MENU ====="

def nextLine ():
    print("")

def create_menu(arr):
    i = 1
    for x in arr:
        print(i, ". ", x)
        i+=1
