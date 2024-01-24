import math


def radians_to_degrees(radians):
    degrees = float(radians) * (180 / math.pi)
    return degrees


def main():
    print("This program calculates radian values into degree values")
    rad = input("Which number do you want to convert? ")
    print(f"The degree value of {rad} is {round(radians_to_degrees(rad), 1)}°.")


if __name__ == '__main__':
    main()
