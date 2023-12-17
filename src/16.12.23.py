def bubbleSortAscending(array):
    smaller = 0
    bigger = 0
    run = True

    for i in range(len(array)):
        run = False

        for y in range(len(array) - 1):
            if array[y] > array[y + 1]:
                bigger = array[y]
                smaller = array[y + 1]
                array[y] = smaller
                array[y + 1] = bigger
                run = True

    return array


def bubbleSortDescending(array):
    smaller = 0
    bigger = 0
    run = True

    for i in range(len(array)):
        run = False

        for y in range(len(array) - 1):
            if array[y] < array[y + 1]:
                bigger = array[y]
                smaller = array[y + 1]
                array[y] = smaller
                array[y + 1] = bigger
                run = True

    return array


def printArray(array):
    for i in range(len(array)):
        print(array[i], end=", ")
    print()


def main():
    x = [4, 2, 7, 1, 9, 5]
    print("unsorted")
    printArray(x)
    print("sorted ascending")
    bubbleSortAscending(x)
    printArray(x)
    print("sorted descending")
    bubbleSortDescending(x)
    printArray(x)


if __name__ == "__main__":
    main()
