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


def shaker_sort_ascending(array):
    start = -1
    end = len(array) - 1
    switched = True

    while switched:
        switched = False
        start += 1
        for i in range(start, end, 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                switched = True
        if not switched:
            break
        switched = False
        end -= 1
        for i in range(end, start, -1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
                switched = True

    return array


def shaker_sort_descending(array):
    start = -1
    end = len(array) - 1
    switched = True

    while switched:
        switched = False
        start += 1
        for i in range(start, end, 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                switched = True
        if not switched:
            break
        switched = False
        end -= 1
        for i in range(end, start, -1):
            if array[i - 1] < array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
                switched = True

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

    asc_shaker = copy.deepcopy(x)
    desc_shaker = copy.deepcopy(x)

    print("sorted shaker sort ascending:")
    start_time = time.time()
    print_array(shaker_sort_ascending(asc_shaker))
    end_time = time.time()
    elapsed_time_shaker_asc = end_time - start_time

    print("sorted shaker sort descending:")
    start_time = time.time()
    print_array(shaker_sort_descending(desc_shaker))
    end_time = time.time()
    elapsed_time_shaker_desc = end_time - start_time

    print(f"The elapsed time for shaker sort ascending equals {elapsed_time_shaker_asc} seconds.")
    print(f"The elapsed time for shaker sort descending equals {elapsed_time_shaker_desc} seconds.")
    print()
    print(f"The elapsed time for the array creation equals {elapsed_time_array_creation} seconds.")


if __name__ == '__main__':
    main()
