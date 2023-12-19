import random
import sys


def random_array(length):
    if length < 1:
        print("Value needs to be larger than 0")
        sys.exit(1)
    array = [0] * length
    for i in range(length):
        array[i] = i + 1
    for i in range(100):
        random.shuffle(array)
    return array


def merge_sort_ascending(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort_ascending(left)
        merge_sort_ascending(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def merge_sort_descending(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort_descending(left)
        merge_sort_descending(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def print_array(array):
    for i in range(len(array)):
        if i < len(array) - 1:
            print(array[i], end=", ")
        else:
            print(array[i], end="")
    print()


def main():
    x = random_array(int(input("How large would you like your array? ")))
    print("unsorted")
    print_array(x)
    print("sorted ascending")
    merge_sort_ascending(x)
    print_array(x)
    print("sorted descending")
    merge_sort_descending(x)
    print_array(x)


if __name__ == "__main__":
    main()
