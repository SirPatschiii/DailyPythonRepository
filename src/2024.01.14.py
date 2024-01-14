def calc_fibonacci_sequence(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]


def main():
    try:
        n = int(input("Please insert the number of elements you wish: "))

        if n <= 0:
            print("Number has to be positive!")
        else:
            result = calc_fibonacci_sequence(n)
            print(f"Fibonacci sequence of the first {n} numbers: {result}")

    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")


if __name__ == "__main__":
    main()
