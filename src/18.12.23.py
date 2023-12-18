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


def insertion_sort_ascending(array):
    for i in range(len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp


def insertion_sort_descending(array):
    for i in range(len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] < temp:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp


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
    insertion_sort_ascending(x)
    print_array(x)
    print("sorted descending")
    insertion_sort_descending(x)
    print_array(x)


if __name__ == "__main__":
    main()
