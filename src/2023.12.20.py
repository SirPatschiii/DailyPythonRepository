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


def quick_sort_ascending(array, low, high):
    if low < high:
        pivot_location = partition_ascending(array, low, high)
        quick_sort_ascending(array, low, pivot_location - 1)
        quick_sort_ascending(array, pivot_location + 1, high)


def quick_sort_descending(array, low, high):
    if low < high:
        pivot_location = partition_descending(array, low, high)
        quick_sort_descending(array, low, pivot_location - 1)
        quick_sort_descending(array, pivot_location + 1, high)


def partition_ascending(array, low, high):
    pivot = array[high]
    left_wall = low

    for i in range(low, high):
        if array[i] <= pivot:
            array[left_wall], array[i] = array[i], array[left_wall]
            left_wall = left_wall + 1

    array[left_wall], array[high] = array[high], array[left_wall]

    return left_wall


def partition_descending(array, low, high):
    pivot = array[high]
    right_wall = low

    for i in range(low, high):
        if array[i] >= pivot:
            array[right_wall], array[i] = array[i], array[right_wall]
            right_wall = right_wall + 1

    array[right_wall], array[high] = array[high], array[right_wall]

    return right_wall


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
    quick_sort_ascending(x, 0, len(x) - 1)
    print_array(x)
    print("sorted descending")
    quick_sort_descending(x, 0, len(x) - 1)
    print_array(x)


if __name__ == "__main__":
    main()
