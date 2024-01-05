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


def radix_sort_ascending(array):
    _BASE = 10
    maximum = max(array)
    factor = 1

    while factor <= maximum:
        partition = [[] for _ in range(_BASE)]
        for i in array:
            idx = (i // factor) % _BASE
            partition[idx].append(i)

        array = []
        for p in partition:
            array += p

        factor *= _BASE

    return array


def radix_sort_descending(array):
    _BASE = 10
    maximum = max(array)
    factor = 1

    while factor <= maximum:
        partition = [[] for _ in range(_BASE)]
        for i in array:
            idx = (i // factor) % _BASE
            partition[idx].append(i)

        array = []
        for p in reversed(partition):
            array += p

        factor *= _BASE

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

    asc_radix = copy.deepcopy(x)
    desc_radix = copy.deepcopy(x)

    print("sorted radix sort ascending:")
    start_time = time.time()
    print_array(radix_sort_ascending(asc_radix))
    end_time = time.time()
    elapsed_time_radix_asc = end_time - start_time

    print("sorted radix sort descending:")
    start_time = time.time()
    print_array(radix_sort_descending(desc_radix))
    end_time = time.time()
    elapsed_time_radix_desc = end_time - start_time

    print(f"The elapsed time for radix sort ascending equals {elapsed_time_radix_asc} seconds.")
    print(f"The elapsed time for radix sort descending equals {elapsed_time_radix_desc} seconds.")
    print()
    print(f"The elapsed time for the array creation equals {elapsed_time_array_creation} seconds.")


if __name__ == '__main__':
    main()
