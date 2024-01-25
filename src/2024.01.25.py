import math
import sys


def solve_for_exponent(base, result):
    if base <= 0 or result <= 0:
        print("Your base and result gotta be positive values!")
        sys.exit(-1)

    exponent = math.log(result, base)

    return exponent


def main():
    print("This program determines the exponent of a number with a given result.")
    base = int(input("Please insert your base: "))
    result = int(input("Please insert your result: "))

    print(f"Your base {base} to the power of {solve_for_exponent(base, result)} equals to your result {result}.")


if __name__ == '__main__':
    main()
