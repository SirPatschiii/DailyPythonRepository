def algorithm_of_euklid(a, b):
    remainder = a % b

    while remainder != 0:
        a = b
        b = remainder
        remainder = a % b

    return b


def main():
    print("This program calculates the greatest common divisor of two numbers")
    first = int(input("Please insert your first number: "))
    second = int(input("Please insert your second number: "))

    divisor = algorithm_of_euklid(first, second)

    print(f"The greatest common divisor of {first} and {second} is {divisor}.")


if __name__ == '__main__':
    main()
