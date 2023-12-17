def selectionSortAscending(array):
    for i in range(len(array)):
        minPos = i
        min = array[minPos]
        for j in range(i + 1, len(array)):
            if array[j] < min:
                minPos = j
                min = array[minPos]

        if minPos != i:
            array[minPos] = array[i]
            array[i] = min

    return array


def selectionSortDescending(array):
    for i in range(len(array)):
        minPos = i
        min = array[minPos]
        for j in range(i + 1, len(array)):
            if array[j] > min:
                minPos = j
                min = array[minPos]

        if minPos != i:
            array[minPos] = array[i]
            array[i] = min

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
    selectionSortAscending(x)
    printArray(x)
    print("sorted descending")
    selectionSortDescending(x)
    printArray(x)


if __name__ == "__main__":
    main()
