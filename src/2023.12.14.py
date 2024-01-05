def calcBMI(height, weight):
    return weight / (height * height)


def main():
    height = input("Wie groß sind Sie? (m) ")
    weight = input("Was sagt Ihnen die Waage wenn Sie darauf stehen? (kg) ")

    print("Ihr BMI beträgt " + str(calcBMI(float(height), float(weight))))


if __name__ == "__main__":
    main()