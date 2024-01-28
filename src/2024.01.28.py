import math


def calculate_distance(x1, x2, y1, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def main():
    point1 = (15, 7)
    point2 = (22, 11)

    length_of_line_segment = calculate_distance(point1[0], point1[1], point2[0], point2[1])
    print(f"The length of the line segment between {point1} and {point2} is: {length_of_line_segment}")


if __name__ == '__main__':
    main()
