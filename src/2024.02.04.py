import random


def generate_random_p_box():
    v_p_box_values = random.sample(range(2**32), 18)

    random.shuffle(v_p_box_values)

    v_p_box = [f'0x{value:08X}' for value in v_p_box_values]

    return v_p_box


def main():
    v_random_p_box = generate_random_p_box()

    print("This program randomly generates the p-box for the blowfish cipher.")
    for i, value in enumerate(v_random_p_box):
        print(f"P{i + 1}: {value}")
    print("However it is important to note, that randomly generating p-boxes isn't considered as very secure.")
    print("For important cases, please use the official p-boxes.")


if __name__ == "__main__":
    main()
