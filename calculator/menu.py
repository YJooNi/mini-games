
display_main_menu = "=== MAIN MENU ==="

def create_menu(arr):
    i = 1
    for x in arr:
        x["id"]= str(i)
        print(f"{i}. {x['option']}") 
        i += 1 

    selection = input("Select an option:")
    for x in arr:
        if x["id"] == selection:
            x["func"]()
            break
    else:
        print(selection, "is not an option!")
        

def create_menu_with_selection(arr):
    i = 1
    for x in arr:
        x["id"]= str(i)
        print(f"{i}. {x['option']}") 
        i += 1 

    selection = input("Select an option:")
    for x in arr:
        if x["id"] == selection:
            x["func"](selection)
            break
    else:
        print(selection, "is not an option!")