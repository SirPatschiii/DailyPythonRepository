import random
import sys
import copy


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


def bucket_sort_ascending(array):
    if len(array) > 9:
        num_buckets = len(array) // 10
    else:
        num_buckets = 1

    buckets = [[] for _ in range(num_buckets)]

    for element in array:
        index = element * num_buckets // (max(array) + 1)
        buckets[index].append(element)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(insertion_sort_ascending(bucket))

    return sorted_array


def bucket_sort_descending(array):
    if len(array) > 9:
        num_buckets = len(array) // 10
    else:
        num_buckets = 1

    buckets = [[] for _ in range(num_buckets)]

    for element in array:
        index = element * num_buckets // (max(array) + 1)
        buckets[index].append(element)

    sorted_array = []
    for bucket in reversed(buckets):
        sorted_array.extend(insertion_sort_descending(bucket))

    return sorted_array


def insertion_sort_ascending(array):
    for i in range(len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array


def insertion_sort_descending(array):
    for i in range(len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and array[j] < temp:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array


def print_array(array):
    for i in range(len(array)):
        if i < len(array) - 1:
            print(array[i], end=", ")
        else:
            print(array[i], end="")
    print()


def main():
    x = random_array(input("How large would you like your array? "))
    print("unsorted")
    print_array(x)

    asc = copy.deepcopy(x)
    desc = copy.deepcopy(x)

    print("sorted ascending")
    print_array(bucket_sort_ascending(asc))

    print("sorted descending")
    print_array(bucket_sort_descending(desc))


if __name__ == "__main__":
    main()
