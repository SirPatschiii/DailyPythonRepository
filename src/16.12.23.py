def bubble_sort_ascending(array):
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


def bubble_sort_descending(array):
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


def print_array(a):
    for i in range(len(a)):
        print(a[i], end=", ")
    print()


def main():
    arr = [4, 2, 7, 1, 9, 5]
    bubble_sort_ascending(arr)
    print_array(arr)
    bubble_sort_descending(arr)
    print_array(arr)


if __name__ == "__main__":
    main()
