def faculty(num):
    if num == 0:
        return 1
    else:
        return num * faculty(num - 1)


def main():
    print("This program is calculating the faculty of a number.")
    num = int(input("Please insert your number: "))

    print(f"The result of the faculty of {num} is {faculty(num)}.")


if __name__ == '__main__':
    main()
