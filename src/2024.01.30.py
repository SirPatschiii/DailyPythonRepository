import sys


global memo


def init_memo():
    for i in range(20):
        for j in range(20):
            memo[i][j] = 0
    for i in range(20):
        memo[i][0] = 1
        memo[i][i] = 1
    return


def calc_binomial_coefficient(n, k):
    global memo

    if n > 19 or k > 19:
        print(f"\nValues are too big!")
        sys.exit(-1)
    if memo[n][k] > 0:
        return memo[n][k]
    memo[n][k] = calc_binomial_coefficient(n - 1, k - 1) + calc_binomial_coefficient(n - 1, k)
    return memo[n][k]


def main():
    global memo
    memo = [[0] * 20 for _ in range(20)]

    init_memo()

    n = int(input("Please insert your first number: "))
    k = int(input("Please insert your second number: "))

    print(f"\nThe result of {n} over {k} is {calc_binomial_coefficient(n, k)}")


if __name__ == '__main__':
    main()
