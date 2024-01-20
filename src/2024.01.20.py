def faculty(num):
    i = 0
    v_faculty = 1

    while i < num:
        i += 1
        v_faculty *= i

    return v_faculty


def main():
    print("This program is calculating the faculty of a number.")
    num = int(input("Please insert your number: "))

    print(f"The result of the faculty of {num} is {faculty(num)}.")


if __name__ == '__main__':
    main()
