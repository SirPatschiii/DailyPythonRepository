import math


def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def calculate_triangle_perimeter(vertices):
    side1 = calculate_distance(vertices[0], vertices[1])
    side2 = calculate_distance(vertices[1], vertices[2])
    side3 = calculate_distance(vertices[2], vertices[0])

    perimeter = side1 + side2 + side3
    return perimeter


def main():
    vertices = [[0, 0], [0, 1], [1, 0]]
    perimeter_value = calculate_triangle_perimeter(vertices)

    print(f"The perimeter of the triangle is: {perimeter_value}")


if __name__ == '__main__':
    main()
