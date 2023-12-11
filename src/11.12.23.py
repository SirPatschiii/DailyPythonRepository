def findBiggestNumber(num1, num2, num3):
    if num1 < num2:
        num1 = num2
    if num1 < num3:
        num1 = num3
    return num1

def main():
    print("Dieses Programm gibt die größte der eingegebenen Zahlen aus")
    num1 = input("Geben Sie bitte Ihre erste Zahl ein: ")
    num2 = input("Geben Sie bitte Ihre zweite Zahl ein: ")
    num3 = input("Geben Sie bitte Ihre dritte Zahl ein: ")
    print("Die größte eingegebene Zahl lautet " + str(findBiggestNumber(num1, num2, num3)))


if __name__ == "__main__":
    main()
