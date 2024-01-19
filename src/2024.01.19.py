def power(base, exponent):
    if exponent == 0:
        return 1

    temp1 = power(base, exponent // 2)
    temp2 = temp1 * temp1

    if exponent % 2 == 0:
        return temp2
    else:
        return base * temp2


def main():
    print("This program is calculating the power of a number.")
    base = int(input("Please insert your base: "))
    exponent = int(input("Please insert your exponent: "))

    print(f"The result of {base} to the power of {exponent} is {power(base, exponent)}.")


if __name__ == '__main__':
    main()
