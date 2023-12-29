import random
import sys
import copy
import time


# creates a random array
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


# bubble sort section
def bubble_sort_ascending(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def bubble_sort_descending(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# selection sort section
def selection_sort_ascending(array):
    for i in range(len(array)):
        min_pos = i
        min = array[min_pos]
        for j in range(i + 1, len(array)):
            if array[j] < min:
                min_pos = j
                min = array[min_pos]

        if min_pos != i:
            array[min_pos] = array[i]
            array[i] = min

    return array


def selection_sort_descending(array):
    for i in range(len(array)):
        max_pos = i
        max = array[max_pos]
        for j in range(i + 1, len(array)):
            if array[j] > max:
                max_pos = j
                max = array[max_pos]

        if max_pos != i:
            array[max_pos] = array[i]
            array[i] = max

    return array


# insertion sort section
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


# merge sort section
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

    return array


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

    return array


# quick sort section
def quick_sort_ascending(array, low, high):
    if low < high:
        pivot_location = partition_ascending(array, low, high)
        quick_sort_ascending(array, low, pivot_location - 1)
        quick_sort_ascending(array, pivot_location + 1, high)

    return array


def quick_sort_descending(array, low, high):
    if low < high:
        pivot_location = partition_descending(array, low, high)
        quick_sort_descending(array, low, pivot_location - 1)
        quick_sort_descending(array, pivot_location + 1, high)

    return array


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


# heap sort section
def heap_sort_ascending(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify_ascending(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify_ascending(array, i, 0)

    return array


def heap_sort_descending(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify_descending(array, n, i)

    for i in range(n - 1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heapify_descending(array, i, 0)

    return array


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


# bucket sort section
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


# prints out the array
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

    asc_bubble = copy.deepcopy(x)
    desc_bubble = copy.deepcopy(x)
    asc_selection = copy.deepcopy(x)
    desc_selection = copy.deepcopy(x)
    asc_insertion = copy.deepcopy(x)
    desc_insertion = copy.deepcopy(x)
    asc_merge = copy.deepcopy(x)
    desc_merge = copy.deepcopy(x)
    asc_quick = copy.deepcopy(x)
    desc_quick = copy.deepcopy(x)
    asc_heap = copy.deepcopy(x)
    desc_heap = copy.deepcopy(x)
    asc_bucket = copy.deepcopy(x)
    desc_bucket = copy.deepcopy(x)

    print("sorted bubble sort ascending:")
    start_time = time.time()
    print_array(bubble_sort_ascending(asc_bubble))
    end_time = time.time()
    elapsed_time_bubble_asc = end_time - start_time

    print("sorted bubble sort descending:")
    start_time = time.time()
    print_array(bubble_sort_descending(desc_bubble))
    end_time = time.time()
    elapsed_time_bubble_desc = end_time - start_time

    print("sorted selection sort ascending:")
    start_time = time.time()
    print_array(selection_sort_ascending(asc_selection))
    end_time = time.time()
    elapsed_time_selection_asc = end_time - start_time

    print("sorted selection sort descending:")
    start_time = time.time()
    print_array(selection_sort_descending(desc_selection))
    end_time = time.time()
    elapsed_time_selection_desc = end_time - start_time

    print("sorted insertion sort ascending:")
    start_time = time.time()
    print_array(insertion_sort_ascending(asc_insertion))
    end_time = time.time()
    elapsed_time_insertion_asc = end_time - start_time

    print("sorted insertion sort descending:")
    start_time = time.time()
    print_array(insertion_sort_descending(desc_insertion))
    end_time = time.time()
    elapsed_time_insertion_desc = end_time - start_time

    print("sorted merge sort ascending:")
    start_time = time.time()
    print_array(merge_sort_ascending(asc_merge))
    end_time = time.time()
    elapsed_time_merge_asc = end_time - start_time

    print("sorted merge sort descending:")
    start_time = time.time()
    print_array(merge_sort_descending(desc_merge))
    end_time = time.time()
    elapsed_time_merge_desc = end_time - start_time

    print("sorted quick sort ascending:")
    start_time = time.time()
    print_array(quick_sort_ascending(asc_quick, 0, len(asc_quick) - 1))
    end_time = time.time()
    elapsed_time_quick_asc = end_time - start_time

    print("sorted quick sort descending:")
    start_time = time.time()
    print_array(quick_sort_descending(desc_quick, 0, len(desc_quick) - 1))
    end_time = time.time()
    elapsed_time_quick_desc = end_time - start_time

    print("sorted heap sort ascending:")
    start_time = time.time()
    print_array(heap_sort_ascending(asc_heap))
    end_time = time.time()
    elapsed_time_heap_asc = end_time - start_time

    print("sorted heap sort descending:")
    start_time = time.time()
    print_array(heap_sort_descending(desc_heap))
    end_time = time.time()
    elapsed_time_heap_desc = end_time - start_time

    print("sorted bucket sort ascending:")
    start_time = time.time()
    print_array(bucket_sort_ascending(asc_bucket))
    end_time = time.time()
    elapsed_time_bucket_asc = end_time - start_time

    print("sorted bucket sort descending:")
    start_time = time.time()
    print_array(bucket_sort_descending(desc_bucket))
    end_time = time.time()
    elapsed_time_bucket_desc = end_time - start_time

    print(f"The elapsed time for bubble sort ascending equals {elapsed_time_bubble_asc} seconds.")
    print(f"The elapsed time for bubble sort descending equals {elapsed_time_bubble_desc} seconds.")
    print()
    print(f"The elapsed time for selection sort ascending equals {elapsed_time_selection_asc} seconds.")
    print(f"The elapsed time for selection sort descending equals {elapsed_time_selection_desc} seconds.")
    print()
    print(f"The elapsed time for insertion sort ascending equals {elapsed_time_insertion_asc} seconds.")
    print(f"The elapsed time for insertion sort descending equals {elapsed_time_insertion_desc} seconds.")
    print()
    print(f"The elapsed time for merge sort ascending equals {elapsed_time_merge_asc} seconds.")
    print(f"The elapsed time for merge sort descending equals {elapsed_time_merge_desc} seconds.")
    print()
    print(f"The elapsed time for quick sort ascending equals {elapsed_time_quick_asc} seconds.")
    print(f"The elapsed time for quick sort descending equals {elapsed_time_quick_desc} seconds.")
    print()
    print(f"The elapsed time for heap sort ascending equals {elapsed_time_heap_asc} seconds.")
    print(f"The elapsed time for heap sort descending equals {elapsed_time_heap_desc} seconds.")
    print()
    print(f"The elapsed time for bucket sort ascending equals {elapsed_time_bucket_asc} seconds.")
    print(f"The elapsed time for bucket sort descending equals {elapsed_time_bucket_desc} seconds.")
    print()
    print(f"The elapsed time for the array creation equals {elapsed_time_array_creation} seconds.")


if __name__ == '__main__':
    main()
