import sys


def check_prime(x):
    if x < 1:
        print("Number has to be greater than 0")
        sys.exit(-1)

    c = 0
    for i in range(1, x):
        if x % i == 0:
            c += 1
        if c == 2:
            break

    if c == 0 or c == 2:
        return False
    else:
        return True


def main():
    x = int(input("Zahl: "))

    tf = check_prime(x)

    match tf:
        case True:
            print(f"Your number {x} is a prime number")
        case False:
            print(f"Your number {x} is not a prime number")


if __name__ == '__main__':
    main()
