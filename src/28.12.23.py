import time


def main():
    start_time = time.time()

    sample: list[int] = []
    for i in range(10_000_000):
        sample.append(i)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Die Ausführungszeit betrug {elapsed_time} Sekunden.")


if __name__ == '__main__':
    main()
