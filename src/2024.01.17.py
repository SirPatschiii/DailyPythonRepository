def get_path_description():
    numbers: list[int] = []

    file = open("src/2024.01.17.txt")
    for line in file:
        path_description = list(line)
        x = 1
        y = 1
        for e in path_description:
            if e == "L":
                if x == 0:
                    continue
                x -= 1
                continue
            if e == "R":
                if x == 2:
                    continue
                x += 1
                continue
            if e == "U":
                if y == 0:
                    continue
                y -= 1
                continue
            if e == "D":
                if y == 2:
                    continue
                y += 1
                continue
        numbers.append(((y * 3) + 1) + x)

    return numbers


def main():
    print(f"Your number is {get_path_description()}")


if __name__ == '__main__':
    main()
