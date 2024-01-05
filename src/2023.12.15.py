def recursiveFunction(n):
    if n < 0:
        return
    print(int(n))
    recursiveFunction(n - 1)


def main():
    n = input("Wie oft soll die Funktion rekursiv ausgeführt werden? ")
    recursiveFunction(int(n))


if __name__ == "__main__":
    main()
