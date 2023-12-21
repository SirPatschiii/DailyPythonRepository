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


def heap_sort_ascending(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify_ascending(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify_ascending(array, i, 0)


def heap_sort_descending(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify_descending(array, n, i)

    for i in range(n - 1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heapify_descending(array, i, 0)


def heapify_ascending(array, n, i):
    max = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and array[max] < array[left_child]:
        max = left_child
    else:
        max = i

    if right_child < n and array[max] < array[right_child]:
        max = right_child

    if max != i:
        array[i], array[max] = array[max], array[i]
        heapify_ascending(array, n, max)


def heapify_descending(array, n, i):
    min = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and array[left_child] < array[min]:
        min = left_child
    else:
        min = i

    if right_child < n and array[right_child] < array[min]:
        min = right_child

    if min != i:
        array[i], array[min] = array[min], array[i]
        heapify_descending(array, n, min)


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
    heap_sort_ascending(x)
    print_array(x)
    print("sorted descending")
    heap_sort_descending(x)
    print_array(x)


if __name__ == "__main__":
    main()
