import switch


def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

num1 = input("Geben Sie bitte eine Zahl ein: ")
num2 = input("Geben Sie bitte noch eine Zahl ein: ")
aritop = input("Was möchten Sie rechnen? (+,-,*,/): ")

num1 = float(num1)
num2 = float(num2)

if (aritop == "+"): print("Addiert ergibt das: " + str(add(num1,num2)))
if (aritop == "-"): print("Subtrahiert gibt das: " + str(subtract(num1,num2)))
if (aritop == "*"): print("Multipliziert gibt das: " + str(multiply(num1,num2)))
if (aritop == "/"): print("Dividiert gibt das: " + str(divide(num1,num2)))
