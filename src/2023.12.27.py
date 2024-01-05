import time


def timer(seconds):
    print(f"Timer gestartet für {seconds} Sekunden.")
    time.sleep(seconds)
    print("Timer abgelaufen!")


def main():
    timer(int(input("Bitte geben Sie eine Anzahl an Sekunden ein: ")))


if __name__ == '__main__':
    main()
