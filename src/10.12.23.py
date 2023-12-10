def build_tree(layers):
    counter = 1
    for i in range(layers):
        for j in range(layers - i, 0, -1):
            print(" ", end="")
        for j in range(counter):
            print("*", end="")
        for j in range(i // 2):
            print(" ", end="")
        print()
        counter = counter + 2


def main():
    layers = int(input("Wie viele Ebenen soll Ihr Weihnachtsbaum haben? "))
    build_tree(layers)


if __name__ == "__main__":
    main()
