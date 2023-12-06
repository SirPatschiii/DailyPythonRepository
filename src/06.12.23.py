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

num1 = float(num1)
num2 = float(num2)

print("Addiert ergibt das: " + str(add(num1,num2)))
print("Subtrahiert gibt das: " + str(subtract(num1,num2)))
print("Multipliziert gibt das: " + str(multiply(num1,num2)))
print("Dividiert gibt das: " + str(divide(num1,num2)))
