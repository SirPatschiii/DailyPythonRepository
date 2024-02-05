import random


def generate_random_s_box():
    v_s_box = [[f'0x{random.randint(0, 2**32 - 1):08X}' for _ in range(256)] for _ in range(4)]
    return v_s_box


def main():
    v_random_s_boxes = generate_random_s_box()

    print("This program randomly generates the s-boxes for the blowfish cipher.")
    for i, s_box in enumerate(v_random_s_boxes):
        print(f"S{i + 1}: {s_box}")
    print("However it is important to note, that randomly generating s-boxes isn't considered as very secure.")
    print("For important cases, please use the official s-boxes.")


if __name__ == "__main__":
    main()
