import random
import sys
import copy
import time


def random_array(length):
    try:
        length = int(length)
    except:
        print("Value needs to be a integer")
        sys.exit(1)

    if length < 1:
        print("Value needs to be larger than 0")
        sys.exit(1)
    array = [0] * length
    for i in range(length):
        array[i] = i + 1
    for i in range(100):
        random.shuffle(array)
    return array


def shell_sort_ascending(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

    return array


def shell_sort_descending(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] < temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

    return array


def print_array(array):
    for i in range(len(array)):
        if i < len(array) - 1:
            print(array[i], end=", ")
        else:
            print(array[i], end="")
    print()
    print()


def main():
    y = input("How large would you like your array? ")

    start_time = time.time()
    x = random_array(y)
    end_time = time.time()
    elapsed_time_array_creation = end_time - start_time

    print()
    print("unsorted array:")
    print_array(x)

    asc_shell = copy.deepcopy(x)
    desc_shell = copy.deepcopy(x)

    print("sorted shell sort ascending:")
    start_time = time.time()
    print_array(shell_sort_ascending(asc_shell))
    end_time = time.time()
    elapsed_time_shell_asc = end_time - start_time

    print("sorted shell sort descending:")
    start_time = time.time()
    print_array(shell_sort_descending(desc_shell))
    end_time = time.time()
    elapsed_time_shell_desc = end_time - start_time

    print(f"The elapsed time for shell sort ascending equals {elapsed_time_shell_asc} seconds.")
    print(f"The elapsed time for shell sort descending equals {elapsed_time_shell_desc} seconds.")
    print()
    print(f"The elapsed time for the array creation equals {elapsed_time_array_creation} seconds.")


if __name__ == '__main__':
    main()
