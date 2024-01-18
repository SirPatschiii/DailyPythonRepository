def power(base, exponent):
    v_power = 1

    while exponent > 0:
        if exponent % 2 == 1:
            v_power = v_power * base
        exponent = exponent // 2
        base = base * base

    return v_power


def main():
    print("This program is calculating the power of a number.")
    base = int(input("Please insert your base: "))
    exponent = int(input("Please insert your exponent: "))

    print(f"The solution of {base} to the power of {exponent} is {power(base, exponent)}.")


if __name__ == '__main__':
    main()
