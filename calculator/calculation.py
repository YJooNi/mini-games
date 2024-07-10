import menu

# =================== basic operations ====================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

# ================= returning value of calculation ===================

def calc(selection, a, b):
    match selection:
        case "1":
            return add(a, b)
        case "2":
           return subtract(a, b)
        case "3":
            return multiply(a, b)
        case "4":
            return divide(a, b)
        
# ========== redundant function for getting A and B values =============

def calc_function(selection):
    while True:
        result = None
        try:
            num1 = input("Enter the first number:")
            num1_float = float(num1)
        except:
            print(num1, "is not a number")
        else:
            while True:
                try:    
                    num2 = input("Enter the second number:")
                    num2_float = float(num2)
                except:
                    print(num2, "is not a number")
                else:
                    result = calc(selection, num1_float,num2_float)
                    print("\nresult:", result)
                    break
        if result is not None:
            break

list_calculation_menu = [{"option": "ADD", "func": calc_function}, {"option": "SUBTRACT", "func": calc_function}, {"option": "MULTIPLY", "func": calc_function}, {"option": "DIVIDE", "func": calc_function},  {"option": "GO BACK", "func": exit}]
# ==================== calculation menu =======================

def calculation_menu():
    while True:
        menu.create_menu(list_calculation_menu)