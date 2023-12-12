def calcRoot(input):
    output = input
    while abs((input - output * output)) > 0.0001:
        output = 0.5 * (input / output + output)
    return round(output, 4)


def main():
    num = input("Aus welcher Zahl möchten Sie die Wurzel ziehen? ")
    print("Die Wurzel von " + str(num) + " beträgt " + str(calcRoot((float(num)))))


if __name__ == "__main__":
    main()
