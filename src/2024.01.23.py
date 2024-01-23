import random
import sys


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


def search_element(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1


def main():
    print("This program performs sequential searches.")
    array = random_array(input("How big should your array be? "))
    v_key = int(input("What number do you search? "))

    v_index = search_element(array, v_key)

    if v_index == -1:
        print("The searched value isn't in the array.")
        sys.exit(-1)
    else:
        print(f"Your number {v_key} is located at the index {v_index}.")


if __name__ == '__main__':
    main()
